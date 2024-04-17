select *
from t1, t2
where t1.pk = t2.pk and 
(t1.column1 != t1.column1 or ...)