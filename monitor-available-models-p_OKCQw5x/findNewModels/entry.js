export default defineComponent({
  async run({ steps, $ }) {

    let new_list = [];

    for(let m of steps.getModels.$return_value) {
      let existingRecord = steps.get_record_or_create.$return_value.find(n => n.name === m.name);
      if(!existingRecord) new_list.push(m);
    }

    return new_list;
  },
})