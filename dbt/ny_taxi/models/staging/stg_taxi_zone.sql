with source as 
(
  select *
  from {{ source('dbt_dev','zones') }}
)
select * from source