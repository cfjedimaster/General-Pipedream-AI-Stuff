
export default defineComponent({
  async run({ steps, $ }) {

    let html = `
<h2>Changes to Google Gemini Models</h2>
<p>
The following changes were detected to the list of available Google Gemini models. 
For more information, see the <a href="https://ai.google.dev/gemini-api/docs/models/gemini">model documentation</a>.
Note that this report does not detect changes to existing models.
</p>

<h2>Removed Models</h2>
    `;

    if(steps.findMissingModels.$return_value.length > 0 ) {

      html += '<ul>';
      steps.findMissingModels.$return_value.forEach(m => {
        html += `<li>${m.displayName} (${m.name})</li>`;        
      });
      html += '</ul>';
    } else {
      html += '<p>No changes detected.</p>';      
    }

    html += '<h2>Added Models</h2>';
    if(steps.findNewModels.$return_value.length > 0 ) {

      html += '<ul>';
      steps.findNewModels.$return_value.forEach(m => {
        html += `<li>${m.displayName} (${m.name})</li>`;        
      });
      html += '</ul>';
    } else {
      html += '<p>No changes detected.</p>';      
    }
    
    return html;
  },
})