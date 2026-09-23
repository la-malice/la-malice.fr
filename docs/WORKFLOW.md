# Cycle de livraison

## Principes

Le checkout principal est `main`, donc le point de publication actuel. Il reste propre. Chaque sujet vit dans un worktree voisin et une branche `feat/`.

```
main propre
  -> start <sujet>
  -> ../la-malice.fr-<sujet> sur feat/<sujet>
  -> revue et validations
  -> merge <sujet> (local, sans publication)
  -> integrate <sujet> (push, verification distante, nettoyage local)
  -> GitHub Pages publie main
```

Cette mecanique n'impose ni framework ni fournisseur. Les controles de build, test, preview et deploiement additionnels seront ajoutes avec l'architecture.

## Worktrees manuels

Depuis `main` propre :

```sh
./scripts/worktree.sh start nom-du-sujet
cd ../la-malice.fr-nom-du-sujet
./scripts/worktree.sh assert nom-du-sujet
```

Le script refuse un `main` ou un sujet sale, un nom ambigu, une branche deja ouverte ailleurs, ou un `main` different de `origin/main` lors de l'integration. Cette contrainte protege les sujets paralleles et les changements non lies.

`merge` sert a une revue locale. En cas de probleme, revenir sur le worktree du sujet et le corriger ; ne pas forcer le merge. `integrate` est volontairement explicite, car il pousse une version publiable. Il ne supprime jamais la branche distante.

## BMad Loop

L'installation BMad fournit les skills de cadrage et de delivery. Loop est un outil d'orchestration, pas un outil de decouverte : ne l'utiliser qu'une fois les stories et le sprint planifies.

Sur chaque machine, lancer une fois `bmad-loop init --project <chemin> --cli codex`, ouvrir Codex dans le projet et accepter la confiance du workspace puis la revue des hooks. La politique locale doit choisir `codex` comme adaptateur.

Avant un premier run, executer `bmad-loop validate --project .`. Un echec pour absence de `sprint-status.yaml` est attendu tant que `bmad-sprint-planning` n'a pas produit le backlog.
