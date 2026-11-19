#!/bin/sh
# A casca do hook do fluxo: o .claude/settings.json a chama no PreToolUse do Bash e do PowerShell, com o gatilho
# no argumento. A lógica e os testes estão em fluxo.py e test_fluxo.py; o porquê, em knowledge/travas.md.
# Nada passa calado: sem Python, ou com o hook quebrado, o agente recebe o aviso de que nada foi conferido.
aqui=$(dirname "$0")
py=""
for p in python3 python py; do
  if "$p" -c "import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)" >/dev/null 2>&1; then py=$p; break; fi
done
avisar() {
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":"%s"}}' "$1"
}
if [ -z "$py" ]; then
  cat >/dev/null
  avisar "O hook do fluxo nao rodou (sem Python 3.9 ou mais novo no PATH) e deixou o comando passar sem conferir. Confira a mao o que as travas cobrariam (knowledge/travas.md); o CI confere de novo."
  exit 0
fi
saida=$(PYTHONUTF8=1 "$py" "$aqui/fluxo.py" "$1")
codigo=$?
if [ "$codigo" -ne 0 ]; then
  avisar "O hook do fluxo saiu com o codigo $codigo e deixou o comando passar sem conferir (knowledge/travas.md)."
  exit 0
fi
printf '%s' "$saida"
exit 0
