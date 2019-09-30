import newsdb

LINE = ''' * '%s' - %s %s'''

if __name__ == '__main__':
    print("1. What are the most popular three articles of all time?")
    posts = "".join(LINE % (title, views, "views") for title, views in
                    newsdb.get_most_popular_three_articles_of_all_time())
    print(posts)

    print("2. Who are the most popular article authors of all time? ")
    posts = "".join(LINE % (name, views, "views") for name, views in
                    newsdb.get_most_popular_article_authors_of_all_time())
    print(posts)

    print("3. On which days did more than 1% of requests lead to errors? ")
    posts = "".join(LINE % (date, percentage, "errors") for
                    date, percentage in newsdb.
                    get_days_where_1percent_plus_of_requests_lead_to_errors())
    print(posts)
