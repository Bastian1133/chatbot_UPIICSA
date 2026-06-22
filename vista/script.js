const sunIcon = '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>';
  const moonIcon = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>';

  const body = document.body;
  const themeToggle = document.getElementById('themeToggle');
  const themeIcon = document.getElementById('themeIcon');
  const themeLabel = document.getElementById('themeLabel');

  function applyTheme(theme) {
    body.setAttribute('data-theme', theme);
    if (theme === 'dark') {
      themeIcon.innerHTML = sunIcon;
      themeLabel.textContent = 'Tema claro';
    } else {
      themeIcon.innerHTML = moonIcon;
      themeLabel.textContent = 'Tema oscuro';
    }
  }

  applyTheme('light');

  themeToggle.addEventListener('click', () => {
    const current = body.getAttribute('data-theme');
    applyTheme(current === 'light' ? 'dark' : 'light');
  });

  // ===== CHAT LOGIC (demo, sin backend conectado) =====
  const chatScroll = document.getElementById('chatScroll');
  const emptyState = document.getElementById('emptyState');
  const messagesEl = document.getElementById('messages');
  const input = document.getElementById('messageInput');
  const sendBtn = document.getElementById('sendBtn');

  function addMessage(text, sender) {
    if (emptyState.style.display !== 'none') {
      emptyState.style.display = 'none';
    }
    const row = document.createElement('div');
    row.className = 'msg-row ' + sender;

    const avatar = document.createElement('div');
    avatar.className = 'msg-avatar ' + sender;
    avatar.textContent = sender === 'bot' ? 'SS' : 'Tú';
    if (sender === 'user') avatar.style.fontSize = '11px';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';

    if (sender === 'bot') {
      bubble.innerHTML = marked.parse(text);
    } else {
      bubble.textContent = text;
    }

    row.appendChild(avatar);
    row.appendChild(bubble);
    messagesEl.appendChild(row);
    chatScroll.scrollTop = chatScroll.scrollHeight;
    return bubble;
  }

  function showTyping() {
    const row = document.createElement('div');
    row.className = 'msg-row bot';
    row.id = 'typingRow';

    const avatar = document.createElement('div');
    avatar.className = 'msg-avatar bot';
    avatar.textContent = 'SS';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.innerHTML = '<div class="typing"><span></span><span></span><span></span></div>';

    row.appendChild(avatar);
    row.appendChild(bubble);
    messagesEl.appendChild(row);
    chatScroll.scrollTop = chatScroll.scrollHeight;
  }

  function removeTyping() {
    const row = document.getElementById('typingRow');
    if (row) row.remove();
  }

  async function sendMessage(text) {
    if (!text.trim()) return;
    addMessage(text, 'user');
    input.value = '';
    showTyping();

    try {
      const response = await fetch('http://127.0.0.1:8000/consulta', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pregunta: text })
      });

      if (!response.ok) {
        throw new Error('Error en la respuesta del servidor');
      }

      const data = await response.json();
      removeTyping();
      addMessage(data.respuesta, 'bot');

    } catch (error) {
      removeTyping();
      addMessage('No fue posible conectar con el servidor. Verifica que el backend esté en ejecución e intenta de nuevo.', 'bot');
      console.error('Error al consultar la API:', error);
    }
  }

  sendBtn.addEventListener('click', () => sendMessage(input.value));
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') sendMessage(input.value);
  });

  document.querySelectorAll('.quick-question').forEach(btn => {
    btn.addEventListener('click', () => sendMessage(btn.dataset.q));
  });