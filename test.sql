with num as (
    select author, num as count(author), sum as sum((total_number_of_pages-pages_read)/speed)
    from book_library
    group by author
),
days as (
    select id, author, book, (total_number_of_pages-pages_read)/speed
    from book_library 
)

select
from num, book_library, days
where num.author = book_library.author and book_library = days.id and num.author = days.author
order by num.num DESC, sum, (book_library.total_number_of_pages - book_library.pages_read)/speed, book_library.book



with num as (
    select author, num as count(author), sum as sum((total_number_of_pages-pages_read)/speed)
    from book_library
    group by author
)

select
from num, book_library
where num.author = book_library.author 
order by num.num DESC, sum, (book_library.total_number_of_pages - book_library.pages_read)/speed, book_library.book

