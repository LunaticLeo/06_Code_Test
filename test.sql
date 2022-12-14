select 
    main.ID,
    main.name,
    (select Division.Divisionname from cb_companydivisions as Division where Division.DivisionID = main.DivisionID),
    (case when main.managerId != null then 
        (select manager.name from maintable_2ZBXT as manager where manager.id = main.managerId) 
    ),
    main.salary
from maintable_2ZBXT as main
order by salary DESC limit 1 offset 2