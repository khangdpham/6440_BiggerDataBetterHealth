queries={
    'create_table':
        'Create table meds (`id` int(11) NOT NULL AUTO_INCREMENT Primary Key, med_id int, count int, mean float, std_dev float, name text);',
    'create_table2':
        'Create table meds_corr (`id` int(11) NOT NULL AUTO_INCREMENT Primary Key, condition_id BIGINT, obs_count int, suggest_med_1 int, suggest_med_1_prob float, suggest_med_2 int default NULL, suggest_med_2_prob float default NULL, suggest_med_3 int default NULL, suggest_med_3_prob float default NULL);',
    'delete_table':
        'Drop table `meds`;',
    'add_row':
        "Insert into meds values(`id`,%s,%s,%s,%s,'%s')",
    'add_row2':
        "Insert into meds_corr values(`id`,%s,%s,%s,%s,%s,%s,%s,%s)",
    'get_row_med_name':
    	"Select * from meds where name='%s'",
    'get_row_med_id':
    	"Select * from meds where med_id=%s"
}
