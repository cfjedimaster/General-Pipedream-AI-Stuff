// To use any npm package, just import it
// import axios from "axios"

export default defineComponent({
  async run({ steps, $ }) {
    // Reference previous step data using the steps object and return data to use it in future steps
    return `Summary of email "${steps.trigger.event.headers.subject}" from ${steps.trigger.event.headers.from.text}:

${steps.generate_text.$return_value[0].candidates[0].output}    
`
  },
})