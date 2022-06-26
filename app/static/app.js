const form = document.getElementById('shorten-form');
const { url: urlInput, submit: submitButton, copy: copyButton } = form;

function setLoading(loading) {
  urlInput.disabled = loading;
  submitButton.disabled = loading;
}

function setCopy(enabled) {
  copyButton.hidden = !enabled;
  submitButton.hidden = enabled;
}

form.onsubmit = async (event) => {
  event.preventDefault();

  // Disable form inputs while loading
  setLoading(true);

  try {
    const response = await fetch('/api/shorten', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url: urlInput.value })
    });

    const { url: shortenedUrl } = await response.json();
    urlInput.value = shortenedUrl;
    setCopy(true);
  } catch (error) {
    alert('Something went wrong');
  }

  setLoading(false);
}

urlInput.oninput = () => {
  if (!copyButton.hidden) {
    setCopy(false);
  }
}

copyButton.onclick = () => {
  urlInput.select();
  urlInput.setSelectionRange(0, urlInput.value.length);

  navigator.clipboard.writeText(urlInput.value);
  alert('URL has been copied');
}