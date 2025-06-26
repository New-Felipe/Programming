// Seleciona o formulário e a área da mensagem
const formulario = document.getElementById('cadastroForm');
const mensagemSection = document.getElementById('mensagem');
const mensagemTexto = document.getElementById('mensagemTexto');

// Função para validar o formulário
function validarFormulario(event) {
    event.preventDefault();  // Evita o envio do formulário

    // Obtém os valores dos campos
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
    const confirmaSenha = document.getElementById('confirmaSenha').value;

    // Verifica se todos os campos foram preenchidos
    if (!nome || !email || !senha || !confirmaSenha) {
        alert("Por favor, preencha todos os campos.");
        return;
    }

    // Verifica se as senhas coincidem
    if (senha !== confirmaSenha) {
        alert("As senhas não coincidem. Tente novamente.");
        return;
    }

    // Exibe a mensagem de sucesso
    formulario.style.display = 'none';
    mensagemSection.style.display = 'block';
    mensagemTexto.textContent = `Cadastro realizado com sucesso, ${nome}!`;

    // Limpa o formulário
    formulario.reset();
}

// Adiciona o evento de envio do formulário
formulario.addEventListener('submit', validarFormulario);
