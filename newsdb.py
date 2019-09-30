import psycopg2

most_popular_three_articles_of_all_time = '''
select
  title,
  views
from
  (
    select
      path,
      count(*) AS Views
    from
      log
    where
      status like '2%' AND
      path in (
          select
            concat('/article/', slug)
          from articles)
    group by
      path
  ) a,
  (
    select
      ar.title,
      au.name,
      CONCAT('/article/', ar.slug) as path
    from
        articles ar
      join
        authors au
      on (ar.author = au.id)
  ) b
where
  a.path = b.path
order by
  views desc
fetch first 3 rows only;
'''

most_popular_article_authors_of_all_time = '''
select
  name,
  sum(views) as views
from
  (
    select
      *
    from
      (
        select
          path,
          count(*) AS Views
        from
          log
        where
          status like '2%' AND
          path in
            (
              select
                concat('/article/', slug)
              from
                articles
            )
        group by
          path
      ) a,
      (
        select
          ar.title,
          au.name,
          CONCAT('/article/', ar.slug) as path
        from
            articles ar
          join
            authors au
          on (ar.author = au.id)
      ) b
    where
      a.path = b.path
  ) as c
group by
  name
order by
  views desc;
'''

days_which_more_than_1percent_of_requests_lead_to_errors = '''
select
  c.date as date,
  c.errors_percentage
from
  (
    select
      a.date,
      a.good_requests + b.bad_requests as total_requests,
      a.good_requests,
      b.bad_requests,
      ROUND(((100.0 * b.bad_requests)/(a.good_requests + b.bad_requests)), 2) \
        as errors_percentage
    from
        (
          select
            TO_CHAR(time, 'Mon DD, YYYY') as date,
            count(*) as good_requests
          from
            log
          where
            status like '2%'
          group by
            TO_CHAR(time, 'Mon DD, YYYY')
        ) a
      join
        (
          select
            TO_CHAR(time, 'Mon DD, YYYY') as date,
            count(*) as bad_requests
          from
            log
          where
            status like '4%'
          group by
            TO_CHAR(time, 'Mon DD, YYYY')
        ) b
      on a.date = b.date
    order by
      errors_percentage desc
  ) c
where
  c.errors_percentage >= 1;
'''

def get_most_popular_three_articles_of_all_time():
    """Return what are the most popular three articles of all time."""
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    cur.execute(most_popular_three_articles_of_all_time)
    results = cur.fetchall()
    conn.close()
    return results

    