# ADR-0001 — Conserver ce depot comme centre de controle avant le choix de stack

**Statut : accepte — 2026-09-23**

## Contexte

Le depot contient une page parking statique publiee par GitHub Pages. La Malice veut concevoir une nouvelle version du site, mais le brief est encore minimal. Le besoin, les contenus, les parcours, la direction visuelle, la stack et l'hebergement ne sont pas decides.

## Decision

Le depot devient le centre de controle du projet : documentation de decouverte, decisions, BMad, Git et cycle de livraison y vivent des maintenant. `main` et son workflow Pages restent la publication actuelle. Aucun choix de framework, CMS, hebergeur, preview, base de donnees ou outil tiers n'est implique par cette decision.

Le travail est isole dans des worktrees `feat/<sujet>`. Une integration explicite dans `main` declenche la publication existante.

## Consequences

- L'equipe peut avancer sur plusieurs sujets sans melanger les changements.
- La page parking reste disponible pendant la decouverte.
- L'architecture et la strategie de preview/deploiement devront faire l'objet d'une ADR ulterieure, basee sur les propositions validees par Emilie.
