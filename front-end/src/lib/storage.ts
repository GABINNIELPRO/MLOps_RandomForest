export type ChatTurn = { role: 'user'|'assistant'; text: string; t: number; tokens?: number };
export type ChatSession = { id: string; title: string; createdAt: number; turns: ChatTurn[] };

const KEY = 'rag_convos';

export function loadSessions(): ChatSession[] {
  try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch { return []; }
}
export function saveSessions(s: ChatSession[]) {
  localStorage.setItem(KEY, JSON.stringify(s));
}
export function upsertSession(sess: ChatSession) {
  const all = loadSessions();
  const i = all.findIndex(x => x.id === sess.id);
  if (i >= 0) all[i] = sess; else all.unshift(sess);
  saveSessions(all);
}
export function newSession(title='Nouvelle conversation'): ChatSession {
  return { id: crypto.randomUUID(), title, createdAt: Date.now(), turns: [] };
}
