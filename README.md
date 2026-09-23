# La Malice — centre de controle du site

Ce depot est le lieu de conception, de production et de publication du futur site de La Malice. Il conserve aujourd'hui la page parking publiee sur GitHub Pages ; le choix de la future stack et de l'hebergement n'est pas encore fait.

## Commencer ici

1. Lire [la gouvernance](docs/PROJECT_GOVERNANCE.md) et [le cycle de livraison](docs/WORKFLOW.md).
2. Lancer la decouverte dans [docs/discovery](docs/discovery/README.md), a partir du brief d'Emilie.
3. Utiliser le skill BMad `bmad-project-context`, puis `bmad-spec`. Ne pas lancer une implementation avant les decisions produit et architecture.

Les sources de verite, les roles et les regles de travail sont dans [AGENTS.md](AGENTS.md).

## Commandes utiles

```sh
# Depuis un checkout propre sur main : creer ou rouvrir un sujet isole.
./scripts/worktree.sh start brief-discovery

# Depuis le worktree du sujet : verifier que le contexte est correct.
./scripts/worktree.sh assert brief-discovery

# Depuis main : integrer localement pour revue, sans publier.
./scripts/worktree.sh merge brief-discovery

# Apres accord explicite : integrer, publier main, verifier origin, nettoyer le worktree local.
./scripts/worktree.sh integrate brief-discovery
```

`main` est la branche publiable : le workflow GitHub Pages existant la deploie. Les choix de preview, staging et hebergement du futur site sont en attente de l'architecture.
