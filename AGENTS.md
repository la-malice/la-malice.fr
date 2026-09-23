# Regles de travail du projet La Malice

## Objet et sources de verite

Ce depot est le centre de controle du futur site de La Malice. La page parking et son deploiement GitHub Pages restent en service tant qu'une decision ne les remplace pas.

| Document | Role |
| --- | --- |
| `AGENTS.md` | regles de collaboration et de qualite |
| `docs/PROJECT_GOVERNANCE.md` | roles et decisions |
| `docs/discovery/` | brief, recherche, hypotheses et propositions |
| `docs/adr/` | decisions techniques et leurs raisons |
| `docs/WORKFLOW.md` | branches, worktrees et livraison |
| `_bmad-output/` | artefacts produits par BMad ; pas une specification manuelle |

Ne pas inventer de besoin, de contenu, de stack ou de prestation. Distinguer un fait source, une hypothese et une decision. Si un document et le runtime divergent, signaler le conflit avant de le corriger.

## Equipe

- Emilie est la sponsor et la decisionnaire communication : elle valide le brief, la priorite, la direction editoriale et les propositions.
- Doudou est le graphiste : il porte la direction visuelle et les assets qui lui sont confies.
- Patrice pilote le produit et la realisation technique : il organise la decouverte, l'architecture, la qualite et les livraisons.

Une validation doit etre tracee dans un document de decouverte ou une ADR ; une absence de reponse n'est pas une validation.

## Decouverte avant architecture

Avant toute implementation, utiliser BMad dans cet ordre :

1. `bmad-project-context` pour cadrer le projet et le brief minimal ;
2. les ateliers BMad de decouverte/ideation utiles ;
3. `bmad-spec` pour formaliser le besoin et les propositions a Emilie ;
4. `bmad-architecture` uniquement apres une direction produit validee ;
5. `bmad-create-epics-and-stories` puis `bmad-sprint-planning` avant Loop.

Le depot peut rester un site statique, changer de stack ou deleguer une partie du besoin a un service tiers. Toute option retenue doit etre motivee par le besoin, le cout, la maintenabilite et l'autonomie de l'equipe, dans une ADR.

## Git, worktrees et livraison

- `main` est la branche de production. Un push sur `main` declenche le deploiement GitHub Pages actuel.
- Tout sujet modifie dans `feat/<cle-kebab>` et son worktree voisin, cree avec `scripts/worktree.sh start <cle-kebab>` depuis un `main` propre.
- Ne jamais developper une fonctionnalite dans le checkout principal `main`.
- `merge` effectue une integration locale pour revue. `integrate` est le geste explicite qui merge, pousse, verifie `origin/main`, puis supprime uniquement le worktree et la branche locaux du sujet. La branche distante est conservee.
- Les messages de commit suivent Conventional Commits, en anglais.
- Ne pas ecraser, stasher, reinitialiser ou supprimer des changements qui ne sont pas ceux du sujet en cours.

## BMad et qualite

- `_bmad/` est gere par l'installateur BMad : ne pas le modifier a la main, sauf `_bmad/custom/config.toml` pour les reglages d'equipe.
- `.agents/skills/`, `.bmad-loop/runs/`, le cache et la politique locale Loop sont generes/localement ignores. Reexecuter l'initialisation sur chaque machine plutot que de les versionner.
- Ne lancer `bmad-loop run` qu'apres sprint planning, avec un backlog versionne et un checkout propre. Les statuts BMad ne remplacent ni les tests ni une validation humaine.
- Toute decision de stack, d'hebergement, de donnees personnelles, de dependance payante ou de publication necessite une ADR et la validation appropriee d'Emilie.
