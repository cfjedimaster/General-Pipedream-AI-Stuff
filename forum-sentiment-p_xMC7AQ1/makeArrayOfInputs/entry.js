/*
Given our RSS result, I translate the kinda gross html-ridden values into an array of strings
*/

export default defineComponent({
  async run({ steps, $ }) {
    return steps.merge_rss_feeds.$return_value.map(r => {
      return r.description.replace(/<.*?>/g, '').replaceAll('&nbsp;',' ').split('. ').slice(0,5).join('. ').trim();
    }).slice(0,10);
  },
})