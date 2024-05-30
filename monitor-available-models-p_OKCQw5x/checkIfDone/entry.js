// To use any npm package, just import it
// import axios from "axios"

export default defineComponent({
  async run({ steps, $ }) {

    if(steps.findMissingModels.$return_value.length === 0 && steps.findNewModels.$return_value.length === 0) $.flow.exit("No changes")
    return;
  },
})