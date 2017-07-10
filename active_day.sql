--postgres sql for active_day calculation of events data

select user_id, 
adj_sent_at::date active_date, 
row_number() over(partition by user_id order by active_date) as active_day

from (select e.user_id, (e.sent_at - f.first_event) as adj_sent_at
  from (select user_id, sent_at from events) e
  join (select user_id, min(sent_at) first_event from events) f on f.user_id = e.user_id)
group by user_id
