const apiKeyInput = document.getElementById('apiKey')
const gameSelect = document.getElementById('gameSelect')
const questionInput = document.getElementById('questionInput')
const askButton = document.getElementById('askButton')
const aiResponse = document.getElementById('aiResponse')
const form = document.getElementById('form')

const markdownToHTML = (text) => {
    const converter = new showdown.Converter()
    return converter.makeHtml(text)
}

const perguntarAI = async (question, game, apiKey) => {
    const model = "gemini-2.0-flash"
const geminiURL = `http://localhost:3001/api/gemini`
    const pergunta = `
        ## Especialidade
        Você é um especialista assistente de meta para o jogo ${game}

        ## Tarefa
        Você deve responder as perguntas do usuário com base no seu conhecimento do jogo, estratégias, build e dicas

        ## Regras
        - Se você não sabe a resposta, responda como 'Não sei' e não tente inventar uma respotas.
        - Se a pergunta não está relacionada ao jogo, responda com 'Essa pergunta não está relacionada ao jogo'
        - Considere a data atual ${new Date().toLocaleDateString()}
        - Faça pesquisas atualizadas sobre o patch atual, baseado na data atual, para dar uma resposta coerente.
        - Nunca responda itens que você não tenha certeza de que existe no patch atual.

        ## Resposta
        - Economize na resposta, seja direto e responda no máximo 500 caracteres.
        - Responda em markdown
        - Não precisa fazer nenhuma saudação ou despedida, apenas responda o que o usuário está querendo.

        ## Exemplos de resposta
        Pergunta do usuário: Arma mais forte entre todas do Cuphead
        resposta: A arma mais forte atual é \n\n **itens:**\n\n coloque os itens ou um único item aqui.\n\n**preço**\n\n coloque o preço das armas aqui.\n\n

        ---
        Aqui está a pergunta do usuário ${question}
    `

    const contents = [{
        role: "user",
        parts: [{
            text: pergunta
        }]
    }]

    const tools = [{
        google_search: {}
    }]

const response = await fetch(geminiURL, {
    method: 'POST',
    headers: {
        'content-type': 'application/json',
        'x-api-key': apiKey
    },
    body: JSON.stringify({
        contents,
        tools
    })
})

if (!response.ok) {
    const errorData = await response.json()
    throw new Error(`API error: ${errorData.error.message || response.statusText}`)
}

const data = await response.json()
return data.candidates[0].content.parts[0].text
}

const enviarFormulario = async (event) => {
    event.preventDefault()
    const apiKey = apiKeyInput.value
    const game = gameSelect.value
    const question = questionInput.value

    if(apiKey == '' || game == '' || question == '') {
        alert("Por favor, preencha todos os campos")
        return
    }

    askButton.disabled = true
    askButton.textContent = "Perguntando..."
    askButton.classList.add('loading')

    // Clear previous response content only when starting a new request
    aiResponse.querySelector('.response-content').innerHTML = ''
    aiResponse.classList.add('hidden')

    try {
        const text = await perguntarAI(question, game, apiKey)
        aiResponse.querySelector('.response-content').innerHTML = markdownToHTML(text)
        aiResponse.classList.remove('hidden')
    } catch(error) {
        console.error("Erro detalhado: ", error)
        if (error instanceof TypeError) {
            aiResponse.querySelector('.response-content').innerHTML = `<p class="error">Erro de rede ou CORS: ${error.message}. Verifique a conexão e as configurações do navegador.</p>`
        } else {
            aiResponse.querySelector('.response-content').innerHTML = `<p class="error">Erro ao obter resposta da IA: ${error.message}</p>`
        }
        aiResponse.classList.remove('hidden')
    } finally {
        askButton.disabled = false
        askButton.textContent = "Perguntar"
        askButton.classList.remove('loading')
    }

}
form.addEventListener('submit', enviarFormulario)
