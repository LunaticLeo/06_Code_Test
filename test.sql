-- with city_count as(
--     select city_id, count(city_id) as num
--     from customer
--     group by city_id
-- ),
-- city_count_country as (
--     select city.name as city_name, country.name as country_name, city_count.num as num
--     from city_count, city, country
--     where city_count.city_id = city.id and country.id = city.country.id
-- )

-- select country_name, city_name, num
-- from city_count_country
-- where num >  (
--     select avg(num)
--     from city_count_country
-- )

with constituency_max as (
    select constituency_id, max(votes) as max
    from results
    group by constituency_id
)
select candidates.party, count(results.constituency_id)
from results, candidates, constituency_max
where constituency_max.constituency_id = results.constituency_id
and constituency_max.max = results.votes
and candidates.id = results.candidate_id
group by candidates.party