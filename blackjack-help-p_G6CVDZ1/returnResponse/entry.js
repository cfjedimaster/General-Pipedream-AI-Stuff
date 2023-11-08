// To return a custom HTTP response, use $.respond() [requires HTTP trigger]
export default defineComponent({
  async run({ steps, $ }) {
    await $.respond({
      status: 200,
      headers: {
        "Content-Type":"application/json"
      },
      body: JSON.stringify(steps.generate_text.$return_value[0].candidates[0].output),
    })
  },
})
