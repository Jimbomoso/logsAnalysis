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