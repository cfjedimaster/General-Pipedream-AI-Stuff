/*
As the name of the step says, this step is meant to take our results and create an email from it.
I will also make an average out of the results, giving numerical values to the possible results. 

I also define colors for each.
*/
export default defineComponent({
  async run({ steps, $ }) {

    let ratings = ["Negative","Somewhat positive","Positive"];
    let totalScore = steps.makeSentimentCalls.$return_value.reduce((prev,v) => {
      return prev + ratings.indexOf(v);
    },0);
    let avg = totalScore / steps.makeSentimentCalls.$return_value.length;

    let generalSentiment = '';
    if(avg < 1) generalSentiment = 'Negative';
    else if(avg < 2) generalSentiment = 'Somewhat positive';
    else if(avg <= 3) generalSentiment = 'Positive';

    let date = new Intl.DateTimeFormat('en-US').format(new Date());
    let email = `
<h2>Forum Sentiment Analysis</h2>
<p>
Report generated on ${date}. Analyzing ${steps.merge_rss_feeds.$return_value.length} recent posts.
</p>

<p>
The general sentiment of the forum is <strong>${generalSentiment}</strong>.
</p>

<table>
<thead>
<tr>
<th>Post</th><th>Sentiment</th>
</tr>
</thead>
<tbody>
    `;

    steps.makeSentimentCalls.$return_value.forEach((s,i) => {
      if(s === '') s = 'No sentiment detected';
      let row = `
<tr>
  <td><a href="${steps.merge_rss_feeds.$return_value[i].link}">${steps.merge_rss_feeds.$return_value[i].title}</a></td><td>${s}</td>
</tr>`;
      email += row;
    });

    email += '</tbody></table>';

    return email;
  },
})