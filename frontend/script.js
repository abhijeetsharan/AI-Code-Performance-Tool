document.getElementById('codeForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const code = document.getElementById('codeInput').value;
  
    const response = await fetch('http://127.0.0.1:5000/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code }),
    });
  
    const result = await response.json();
    const resultDiv = document.getElementById('result');
    if (result.error) {
      resultDiv.innerHTML = `<p style="color: red;">Error: ${result.error}</p>`;
    } else {
      resultDiv.innerHTML = `
        <h3>Analysis</h3>
        <p><strong>Warnings:</strong> ${result.warnings.join(', ') || 'None'}</p>
        <p><strong>Suggestions:</strong> ${result.suggestions.join(', ') || 'None'}</p>
      `;
    }
  });
  