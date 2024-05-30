
export default defineComponent({
  async run({ steps, $ }) {

    let API_KEY = process.env.GOOGLE_API_KEY;
    let modelReq = await fetch(`https://generativelanguage.googleapis.com/v1/models?key=${API_KEY}`);
    let models = (await modelReq.json()).models;

    return models;
  },
})