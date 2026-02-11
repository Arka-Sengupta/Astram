import { useState } from 'react'
import { Send, Bot, User, Cpu } from 'lucide-react'
import ReactMarkdown from 'react-markdown'

function App() {
    const [input, setInput] = useState('')
    const [messages, setMessages] = useState([])
    const [loading, setLoading] = useState(false)

    const sendMessage = async () => {
        if (!input.trim()) return

        const userMsg = { role: 'user', content: input }
        setMessages(prev => [...prev, userMsg])
        setInput('')
        setLoading(true)

        try {
            const res = await fetch('/api/chat', { // using proxy
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMsg.content })
            })
            const data = await res.json()
            setMessages(prev => [...prev, { role: 'assistant', content: data.response }])
        } catch (error) {
            setMessages(prev => [...prev, { role: 'assistant', content: "Error: Could not reach agent." }])
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="min-h-screen bg-gray-900 text-gray-100 flex flex-col font-sans">
            <header className="bg-gray-800 p-4 border-b border-gray-700 flex items-center gap-3 shadow-md">
                <div className="bg-blue-600 p-2 rounded-lg">
                    <Cpu size={24} className="text-white" />
                </div>
                <h1 className="text-xl font-bold tracking-tight">Chat with Astram!</h1>
                <span className="ml-auto text-xs bg-gray-700 px-2 py-1 rounded text-gray-400">made by Arka Sengupta</span>
            </header>

            <main className="flex-1 overflow-y-auto p-4 space-y-4 scroll-smooth">
                {messages.length === 0 && (
                    <div className="flex flex-col items-center justify-center h-full text-gray-500 gap-4 opacity-50">
                        <Bot size={64} />
                        <p className="text-lg">Throw me any coding related queries lets see what my brain responds</p>
                    </div>
                )}

                {messages.map((msg, idx) => (
                    <div key={idx} className={`flex gap-4 ${msg.role === 'user' ? 'flex-row-reverse' : ''}`}>
                        <div className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 
              ${msg.role === 'user' ? 'bg-blue-600' : 'bg-green-600'}`}>
                            {msg.role === 'user' ? <User size={16} /> : <Bot size={16} />}
                        </div>
                        <div className={`max-w-[80%] p-4 rounded-2xl shadow-sm text-sm leading-relaxed
              ${msg.role === 'user'
                                ? 'bg-blue-600 text-white rounded-tr-none whitespace-pre-wrap'
                                : 'bg-gray-800 border border-gray-700 text-gray-200 rounded-tl-none prose prose-invert prose-sm max-w-none'}`}>
                            {msg.role === 'user' ? (
                                msg.content
                            ) : (
                                <ReactMarkdown>{msg.content}</ReactMarkdown>
                            )}
                        </div>
                    </div>
                ))}

                {loading && (
                    <div className="flex gap-4">
                        <div className="w-8 h-8 rounded-full bg-green-600 flex items-center justify-center shrink-0 animate-pulse">
                            <Bot size={16} />
                        </div>
                        <div className="bg-gray-800 border border-gray-700 p-4 rounded-2xl rounded-tl-none flex items-center gap-2 text-gray-400 text-sm">
                            <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></span>
                            <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-75"></span>
                            <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-150"></span>
                        </div>
                    </div>
                )}
            </main>

            <div className="p-4 bg-gray-800 border-t border-gray-700">
                <div className="max-w-4xl mx-auto flex gap-2">
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
                        placeholder="Type your instruction..."
                        className="flex-1 bg-gray-900 border border-gray-600 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-white placeholder-gray-500 transition-all"
                        disabled={loading}
                    />
                    <button
                        onClick={sendMessage}
                        disabled={loading || !input.trim()}
                        className="bg-blue-600 hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed text-white p-3 rounded-xl transition-colors flex items-center justify-center group"
                    >
                        <Send size={20} className="group-hover:translate-x-0.5 transition-transform" />
                    </button>
                </div>
            </div>
        </div>
    )
}

export default App
