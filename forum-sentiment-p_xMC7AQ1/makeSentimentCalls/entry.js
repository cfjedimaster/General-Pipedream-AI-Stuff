//const { TextServiceClient } = require("@google-ai/generativelanguage");
import { TextServiceClient } from '@google-ai/generativelanguage';
//const { GoogleAuth } = require("google-auth-library");
import { GoogleAuth } from 'google-auth-library';

async function getSentiment(s, key) {
  const MODEL_NAME = "models/text-bison-001";
  const client = new TextServiceClient({
    authClient: new GoogleAuth().fromAPIKey(key),
  });

  return 'ok';
}

export default defineComponent({


  async run({ steps, $ }) {
    // Reference previous step data using the steps object and return data to use it in future steps
    return getSentiment('foo', process.env.PALM_KEY);
  },
})