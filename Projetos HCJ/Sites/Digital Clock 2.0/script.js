function updateClock() {
    const format = document.getElementById('format').value;
    const now = new Date();
    let hours = now.getHours();
    const minutes = String(now.getMinutes()).padStart(2, '0');

    if (format === '12') {
        const ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours ? hours : 12; // O horário 0 deve ser 12
        document.getElementById('clock').textContent = `${hours}:${minutes} ${ampm}`;
    } else {
        document.getElementById('clock').textContent = `${String(hours).padStart(2, '0')}:${minutes}`;
    }
}

// Atualiza o relógio a cada segundo
setInterval(updateClock, 1000);

// Atualiza o relógio na primeira execução
updateClock();

// Atualiza o relógio quando o formato é alterado
document.getElementById('format').addEventListener('change', updateClock);