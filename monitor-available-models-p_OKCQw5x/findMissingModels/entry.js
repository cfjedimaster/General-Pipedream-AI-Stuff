export default defineComponent({
  async run({ steps, $ }) {

    let old_list = steps.get_record_or_create.$return_value;
    console.log('old list', old_list);

    let removed_list = [];
    
    for(let m of old_list) {
      let existingRecord = steps.getModels.$return_value.find(n => n.name === m.name);
      if(!existingRecord) removed_list.push(m);
    }

    return removed_list;
  },
})