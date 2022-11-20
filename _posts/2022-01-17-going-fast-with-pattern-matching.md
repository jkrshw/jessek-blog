Title: Going Fast with Oracle Pattern Matching
Date: 2022-01-17 10:20
Tags: oracle, performance, pattern, cern
Slug: going-fast-with-oracle-pattern-matching

The documentation for [Oracle Pattern Matching](https://docs.oracle.com/en/database/oracle/oracle-database/19/dwhsg/sql-pattern-matching-data-warehouses.html) queries is a bit hard to follow, and as soon as regular
expressions are mentioned things stop making sense. It's then no surprise if you haven't heard of, 
or don't know how to use, this very powerful query feature.

It's a feature best explained by examples and the Oracle documentation contains several. From 
detecting dips and peaks in the stock market to analysing audit logs. In BC, a common use case might 
be to merge consecutive periods in to a single period that covers all the individual periods.

Foundation Merged Contract History
----------------------------------

Foundation contains a table cf_contract_history_tab that contains all of the different contracts and 
assignments that a person has had at CERN. The cf_merged_contract_history view merges the consecutive 
primary assignments for each person in to single periods. This makes it easy to determine from when a 
person had a particular status.

We can see this in a simple example:

### Contract History
|| Person ID || Status || Start Date || End Date ||
| 123456 | USER | 2001-01-01 | 2004-03-31 |
| 123456 | USER | 2004-04-01 | 2010-01-31 |
| 123456 | STAFF | 2010-02-01 |	

### Merged Contract History
|| Person ID || Status || Start Date || End Date ||
| 123456 | USER | 2001-01-01 | 2010-01-31 |
| 123456 | STAFF | 2010-02-01 | |

The 2 consecutive USER contracts have been merged in to a single period followed by a STAFF contract.
Of course, the source table would contain the contract history for many other people as well as 
secondary assignments, and possibly multiple disjointed periods of the same type.

How is this achieved? When I consider database performance, I like to imagine how I would solve the 
problem if each row was a physical card and I had to arrange them by hand to get the desired result. 
\My approach might be to get all of the cards for a particular person, order them by contract start 
date, then starting with the first card, check if the next card is for the same logical contract, 
that is the start date follows from the previous card's end date and they are both for the same 
status, and then continue until there is a break in the sequence. I can then take the contract start 
date from the first card I found and the end date from the last card in the sequence to create a new 
card that covers the full period.

This is how Oracle's pattern matching works. It's also a similar strategy to analytical functions. By using some partitioning and ordering, we can calculate complex things with only one pass of the data.

Before pattern matching however, this approach was impossible.

Joins and Sub Queries
---------------------

The pattern matching feature was added in Oracle 12c, prior to that, one approach to solve the 
merging problem in SQL is to use joins and sub queries.

Consider the same physical approach as before. I get all of the cards for a person, they are not 
ordered. I take two cards at random and perform a series of checks. First I make sure the cards are 
for the same status, and that the first card comes before the second card. I then check the other 
cards to see if there are any that come before or after this pair, I make sure all of the other cards 
that are in between the pair have the same status, and that there are no gaps. If all of these 
conditions hold, I have found the start and end contract periods. Remember the 2 cards are picked at 
random, so for every true pair there are many combinations of pairs that are not correct.

This is the SQL to perform this query. It is a bit more complicated (as real life always is) because 
in 2001 there was a change in status, PDSA became PDAS, so the view needs to handle that.

```sql
select con_start.pidcfcontract_histo
      ,con_start.percfcontract_histo
      ,con_start.stdcfcontract_histo
      ,con_end.endcfcontract_histo
      ,con_end.pclcfcontract_histo
  from cf_contract_histo_tab con_start
      ,cf_contract_histo_tab con_end
  where 1 = 1
    and con_start.pricfcontract_histo = 'Y'
    and con_end.pricfcontract_histo = 'Y'
    and con_start.pidcfcontract_histo = con_end.pidcfcontract_histo
    and con_start.asscfcontract_histo = con_end.asscfcontract_histo
    and ( con_start.stdcfcontract_histo <= con_end.endcfcontract_histo
          or con_end.endcfcontract_histo is null
        )
    and ( con_start.pclcfcontract_histo = con_end.pclcfcontract_histo
          or ( con_end.stdcfcontract_histo >= to_date( '20010101', 'YYYYMMDD' )
               and ( con_start.pclcfcontract_histo = 'PDSA' and con_end.pclcfcontract_histo = 'PDAS' )
             )
        )
    -- make sure that we have no preceding period with same assignment
    --
    and not exists ( select null
                       from cf_contract_histo_tab con_before
                       where 1 = 1
                         and trunc( con_start.stdcfcontract_histo ) - trunc( con_before.endcfcontract_histo ) = 1
                         and ( con_end.pclcfcontract_histo = con_before.pclcfcontract_histo
                               or ( con_end.stdcfcontract_histo >= to_date( '20010101', 'YYYYMMDD' )
                                    and con_before.stdcfcontract_histo < to_date( '20010101', 'YYYYMMDD' )
                                    and ( con_before.pclcfcontract_histo = 'PDSA' and con_end.pclcfcontract_histo = 'PDAS' )
                                  )
                             )
                         and con_start.asscfcontract_histo = con_before.asscfcontract_histo
                         and con_start.percfcontract_histo = con_before.percfcontract_histo
                         and con_before.pricfcontract_histo = 'Y'
                   )
    -- make sure that we have no follow-up period with the same assignment
    --
    and not exists ( select null
                       from cf_contract_histo_tab con_after
                       where 1 = 1
                         and trunc( con_after.stdcfcontract_histo ) - trunc( con_end.endcfcontract_histo ) = 1
                         and ( con_start.pclcfcontract_histo = con_after.pclcfcontract_histo
                               or ( con_after.stdcfcontract_histo >= to_date( '20010101', 'YYYYMMDD' )
                                    and con_start.stdcfcontract_histo < to_date( '20010101', 'YYYYMMDD' )
                                    and ( con_start.pclcfcontract_histo = 'PDSA' and con_after.pclcfcontract_histo = 'PDAS' )
                                  )
                             )
                         and con_start.asscfcontract_histo = con_after.asscfcontract_histo
                         and con_start.percfcontract_histo = con_after.percfcontract_histo
                         and con_after.pricfcontract_histo = 'Y'
                   )
    -- make sure that there is no period in between the start and end that is different
    --
    and not exists ( select null
                       from cf_contract_histo_tab con_within
                       where con_start.percfcontract_histo = con_within.percfcontract_histo
                         and con_within.pricfcontract_histo = 'Y'
                         and con_within.stdcfcontract_histo between con_start.stdcfcontract_histo
                                                                and nvl( con_end.endcfcontract_histo, to_date( '31124712', 'DDMMYYYY' ) )
                         and nvl( con_within.endcfcontract_histo, to_date( '31124712', 'DDMMYYYY' ) ) between con_start.stdcfcontract_histo
                                                                                                          and nvl( con_end.endcfcontract_histo, to_date( '31124712', 'DDMMYYYY' ) )
                         and ( ( con_start.pclcfcontract_histo <> con_within.pclcfcontract_histo
                                 and con_end.pclcfcontract_histo <> con_within.pclcfcontract_histo
                               )
                               or con_start.asscfcontract_histo <> con_within.asscfcontract_histo
                             )
                   )
    -- check that there is no interruption of more than 1 day in between the start and end contrat period
    --
    and not exists ( select null
                       from cf_contract_histo_tab before_hole
                       where con_start.percfcontract_histo = before_hole.percfcontract_histo
                         and before_hole.pricfcontract_histo = 'Y'
                         and ( before_hole.endcfcontract_histo < con_end.endcfcontract_histo
                               or ( con_end.endcfcontract_histo is null
                                    and before_hole.endcfcontract_histo is not null
                                  )
                             )
                         and ( before_hole.endcfcontract_histo >= con_start.stdcfcontract_histo
                               or before_hole.endcfcontract_histo is null
                             )
                         and not exists ( select null
                                            from cf_contract_histo_tab hole
                                            where hole.percfcontract_histo = before_hole.percfcontract_histo
                                              and hole.pricfcontract_histo = 'Y'
                                              and trunc( hole.stdcfcontract_histo ) - trunc( before_hole.endcfcontract_histo ) = 1
                                        )
                   )
```

Match Recognize
---------------

Here is the same query rewritten to use Pattern Matching

```sql
SELECT
    pidcfcontract_histo AS person_id,
    cern_id,
    start_date,
    end_date,
    status
FROM (SELECT * FROM cf_contract_histo_tab where pricfcontract_histo = 'Y')
         MATCH_RECOGNIZE (
             PARTITION BY pidcfcontract_histo
             ORDER BY stdcfcontract_histo
             MEASURES
                 FIRST(percfcontract_histo) AS cern_id,
                 FIRST(stdcfcontract_histo) AS start_date,
                 LAST(endcfcontract_histo) AS end_date,
                 LAST(pclcfcontract_histo) AS status
             PATTERN (A (B|C)*)
             DEFINE
                 B AS (B.asscfcontract_histo = PREV(asscfcontract_histo)
                     AND B.pclcfcontract_histo = PREV(pclcfcontract_histo)
                     AND B.stdcfcontract_histo = PREV(endcfcontract_histo + 1)),
                 C AS (C.asscfcontract_histo = PREV(asscfcontract_histo)
                     AND C.pclcfcontract_histo = 'PDAS'
                     AND PREV(pclcfcontract_histo) = 'PDSA'
                     AND C.stdcfcontract_histo >= date'2001-01-01'
                     AND C.stdcfcontract_histo = PREV(endcfcontract_histo + 1)))
             )
```

Not much of this looks like normal SQL so let's break it down:

First we specify our PARTITION BY key and ORDER, in this case the person id pidcfcontract_histo and 
start date stdcfcontract_histo.

The next logical part of the query is to define the categories of matching so let's skip down the 
query to the DEFINE section. Category B is the standard case, where the row has the same Assignment 
ID and Status as the previous row, and the Start Date is 1 day after the previous row's End Date. 
Category C is the special case of PDSA to PDAS. We could call these something other than B, C but 
naming things is hard.

Now move up slightly in the query to the PATTERN. This is the regular expression, except instead of 
operating over a set of characters like we're used to, it is operating over the different categories 
we have defined. Category A is not defined so any row can be considered category A. Our pattern says 
we want an A row, followed by 0 or more B or C rows.

Moving up the query a bit more we have the MEASURES. Here we specify what the output row should be. 
In our case, we want the Start Date and CERN ID of the first row, and the End Date and Status of the 
last row.

One last note is that in the FROM we have a nested query. MATCH_RECOGNIZE doesn't support a WHERE 
clause, so we need to filter out all the secondary assignments first before running the pattern matching.

Performance
-----------

The query plan for the join query is quite complex with 2 FULL table lookups (for the join) and 4 
index lookups (for each check). The plan for the pattern match query is quite simple, a single FULL 
table lookup and a SORT.

Selecting all rows from the pattern match query takes around 1 second vs. 75-120 seconds for the 
join query.

This is not really a fair comparison since this view is not usually accessed in full and instead a 
person id is provided. When querying for a specific person, both views return results within 20-30ms, 
thanks to the index on person id.

Using the Autotrace feature in SQL Developer we can see how much work the database has to do to 
respond. For the pattern match query there were 5 buffer gets and an elapsed time of 104 vs. 398 buffer 
gets and an elapsed time of 1800-2000. The pattern match query appears to be much more efficient.

Conclusion
----------

Pattern Matching is at first a complicated looking syntax that seems impossible to follow, but once 
you understand the structure, it's not such a complicated feature that can perform operations that 
were previously very complex and inefficient to achieve.