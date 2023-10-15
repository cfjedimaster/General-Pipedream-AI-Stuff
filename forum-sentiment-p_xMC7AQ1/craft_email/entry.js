/*
As the name of the step says, this step is meant to take our results and create an email from it.
I will also make an average out of the results, giving numerical values to the possible results. 

I also define colors for each.
*/
export default defineComponent({
  async run({ steps, $ }) {
    // Reference previous step data using the steps object and return data to use it in future steps
    return steps.trigger.event
  },
})
