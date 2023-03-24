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

-- with constituency_max as (
--     select constituency_id, max(votes) as max
--     from results
--     group by constituency_id
-- )
-- select candidates.party, count(results.constituency_id)
-- from results, candidates, constituency_max
-- where constituency_max.constituency_id = results.constituency_id
-- and constituency_max.max = results.votes
-- and candidates.id = results.candidate_id
-- group by candidates.party


with t as (
    select readings.account_id, readings.amount as amount, tariffs.name as tariff_name, tariffs.cost, readings.amount * tariffs.cost as price
    from tariffs, readings
    where readings.tariff_id = tariffs.id
),
t2 as (
    select account_id, max(cost) as max_cost, sum(amount) as consumption, sum(price) as total_cost
    from t
    group by account_id
    
),
t3 as (
    select t.account_id, t.tariff_name as highest_tariff, t2.consumption, t2.total_cost
    from t, t2
    where t.account_id = t2.account_id and 
    t.cost = t2.max_cost
)
select accounts.username, accounts.email, t3.highest_tariff, t3.consumption, round(t3.total_cost,2)
from t3, accounts
where t3.account_id = accounts.id
order by accounts.username






