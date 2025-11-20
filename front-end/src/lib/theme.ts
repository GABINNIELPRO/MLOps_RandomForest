export type Theme = 'light'|'dark'|'system';
const KEY = 'rag_theme';

const prefersDark = () =>
  window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

export function getTheme(): Theme {
  return (localStorage.getItem(KEY) as Theme) || 'system';
}

export function applyTheme(t: Theme) {
  const root = document.documentElement;
  const finalDark = t === 'dark' || (t === 'system' && prefersDark());
  root.classList.toggle('dark', finalDark);
  localStorage.setItem(KEY, t);
}

export function initThemeOnce() {
  applyTheme(getTheme());
}
