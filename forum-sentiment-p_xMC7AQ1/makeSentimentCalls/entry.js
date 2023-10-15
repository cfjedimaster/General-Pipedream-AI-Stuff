//const { TextServiceClient } = require("@google-ai/generativelanguage");
import { TextServiceClient } from '@google-ai/generativelanguage';
//const { GoogleAuth } = require("google-auth-library");
import { GoogleAuth } from 'google-auth-library';

async function getSentiment(s, key) {
  const MODEL_NAME = "models/text-bison-001";
  const client = new TextServiceClient({
    authClient: new GoogleAuth().fromAPIKey(key),
  });

  const promptString = `Tell me whether the following sentence's sentiment is positive or negative or something in between.
  Sentence I would love to walk along the beach.
  Sentiment Somewhat positive
  Sentence I love my new record player
  Sentiment Positive
  Sentence I really hate it when my brother steals my things
  Sentiment Negative
  Sentence ${s}
  Sentiment
  `;
  const stopSequences = [];

  let result = await client.generateText({
    // required, which model to use to generate the result
    model: MODEL_NAME,
    // optional, 0.0 always uses the highest-probability result
    temperature: 0.5,
    // optional, how many candidate results to generate
    candidateCount: 1,
    // optional, number of most probable tokens to consider for generation
    top_k: 40,
    // optional, for nucleus sampling decoding strategy
    top_p: 0.95,
    // optional, maximum number of output tokens to generate
    max_output_tokens: 1024,
    // optional, sequences at which to stop model generation
    stop_sequences: stopSequences,
    // optional, safety settings
    safety_settings: [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
    prompt: {
      text: promptString,
    },
  });

  //To do, check for len of candidates and if zero, return ''
  return result[0].candidates[0].output;
}

export default defineComponent({


  async run({ steps, $ }) {
    let promises = [];
    steps.makeArrayOfInputs.forEach(p => {
      promises.push(getSentiment(p, process.env.PALM_KEY))
    });
    console.log('made my calls');

    let initialresults = await Promise.allSettled(promises);
    let results = [];
    initialResults.forEach(r => {
      if(r.status === 'fulfilled') {
          results.push(r.value);
      } else {
        results.push('Error');
      }
    });

    return results;
  },
})
