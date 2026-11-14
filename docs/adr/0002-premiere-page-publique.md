# ADR-0002 — Première page publique statique

**Statut : accepté — 14 novembre 2026.** Patrice confirme la validation par Émilie du périmètre, du maintien de GitHub Pages et de la mise à jour manuelle. Émilie demande la mise en ligne de la version présentée le 14 novembre 2026 et prévoit des commentaires ensuite ; Patrice autorise le déploiement.

## Contexte

Une première page vivante doit présenter la troupe, les dates, des publications Instagram et les liens utiles rapidement. Le dépôt contient une page HTML statique, un domaine et un workflow GitHub Actions déployant Pages depuis `main`. Les médias, dates et responsable de leur actualisation restent à confirmer. L’autonomie des bénévoles est un besoin identifié ; leurs accès et compétences ne sont pas établis.

## Solution retenue par Patrice

Patrice et Émilie retiennent le 14 novembre la solution suivante pour cette première version : conserver une page statique HTML/CSS, avec JavaScript limité aux interactions utiles, sans serveur applicatif ni base de données ; utiliser le dépôt et GitHub Pages déjà en place. Les spectacles et la sélection de publications Instagram sont préparés manuellement depuis des informations validées. Les publications pointent vers leurs sources ; aucune synchronisation automatique n’est promise. Prévoir une procédure explicite de modification et de publication, et nommer un responsable et un relais avant lancement.

Séparer les fichiers publics de conception et documents internes : le workflow actuel fournit `path: .` à l’action de publication. Définir et vérifier une liste explicite des fichiers effectivement publiables avant de déployer la nouvelle version ; ne pas supposer qu’une règle `.gitignore` protège un fichier publié. Conserver les routes et ressources existantes nécessaires, dont la page du festival, et vérifier le domaine configuré ainsi que HTTPS après publication.

Prévisualisation : utiliser un serveur local dans le worktree et fournir un accès de revue adapté. Ne pas modifier le domaine public pour la prévisualisation. Les détails de l’accès distant restent à établir. Livraison : contrôles puis intégration explicite et déploiement depuis `main` ; surveiller l’exécution Pages et vérifier la page publique. Préparer une marche arrière par nouveau commit restaurant la version précédente, sans réécrire l’historique partagé.

## Options examinées

- **Statique existant — recommandé :** peu de changements, pas de nouveau fournisseur ni d’application à maintenir ; la mise à jour exige un accès et une procédure Git, donc l’autonomie de l’équipe doit être démontrée.
- **CMS ou service hébergé :** potentiellement plus accessible à un bénévole, mais nécessite choix de fournisseur, coût, accès, paramétrage et maintenance ; à étudier si la mise à jour manuelle ne convient pas.
- **Agenda et publications synchronisés :** réduisent des ressaisies potentielles, mais exigent une source publique fiable, des règles et une maintenance supplémentaires ; reportés.

## Conséquences et décisions ouvertes

Pas de promesse de coût nul : vérifier les conditions applicables au compte existant. L’accès en écriture au dépôt et le processus d’actualisation doivent être validés avec l’équipe. Aucun nouveau compte ni service n’est créé par cette proposition. Les modalités d’intégration visuelle d’Instagram, les droits des médias et le traitement des contenus manquants restent à confirmer. La direction artistique relève de Doudou et les contenus et la publication finale d’Émilie.

## Sources

- Dépôt : `index.html`, `.github/workflows/`, `CNAME`, `docs/adr/0001-centre-de-controle-independant-de-la-stack.md`.
- Documentation GitHub Pages : https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages et https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site.
