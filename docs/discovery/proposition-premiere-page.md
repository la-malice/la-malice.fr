# Proposition d’epic — Première page publique La Malice

Statut : cadrage validé, 14 novembre 2026. Périmètre validé par Émilie selon confirmation de Patrice ; contenus définitifs, direction visuelle et version à publier restent à revoir avec Émilie et Doudou. Ce document prépare les artefacts BMAD et ne remplace pas leurs prérequis.

## Objectif

Permettre à une personne qui découvre La Malice sur la Côte basque de comprendre son activité, de trouver les spectacles annoncés et de suivre ou contacter la troupe, grâce à une page accueillante et lisible sur téléphone.

## Sources

Messages d’Émilie transmis par Patrice : présence web rapide, page dynamisée avec photos, piste monopage, référencement local, réemploi des contenus existants. Périmètre proposé et accepté par Patrice le 14 novembre. Brief existant en brouillon dans le worktree `feat/web-improv-research` ; page parking `index.html` et liens existants dans `main`. Patrice confirme le 14 novembre la validation de cette proposition par Émilie ; cette validation du périmètre ne vaut pas approbation des contenus ni de la version finale.

## Découpage proposé

### 1. Cadrer et préparer la livraison

En tant que responsable du projet, je veux un périmètre et une solution simples documentés pour livrer rapidement une page maintenable.

- Formaliser le besoin avec `bmad-spec`, puis la décision d’architecture adaptée à cette première version, après validation de la direction produit par Émilie.
- Définir avec Doudou l’intention visuelle et les éléments à réutiliser ; consigner les validations.
- Établir les stories et le sprint selon le workflow du dépôt ; désigner la personne qui actualisera les dates et les publications.
- Préserver la page en service pendant la préparation. Le maintien de l’existant statique et de GitHub Pages est une proposition à documenter, pas une décision déjà prise pour le futur site.

### 2. Présenter la troupe et faciliter les parcours

En tant que visiteur, je veux comprendre rapidement qui est La Malice et accéder aux informations utiles.

- Une page adaptée au mobile et à l’ordinateur comprend accueil, navigation par ancres, présentation de la troupe et liens utiles vérifiés.
- L’accueil associe une introduction courte, un visuel et un accès clair aux spectacles. Les textes dérivés de l’existant sont soumis à Émilie.
- La piste sombre et bleue est une proposition à valider avec Doudou et Émilie ; les médias provisoires sont identifiés pendant la prévisualisation.
- Le contenu reste lisible et navigable au clavier, avec des textes alternatifs adaptés aux images et des liens explicites.

### 3. Montrer les spectacles et l’actualité

En tant que spectateur, je veux voir les dates annoncées et l’activité récente de la troupe pour choisir une sortie et la suivre.

- Chaque spectacle fourni et publiable affiche son intitulé, sa date et son lieu ; sa réservation est liée si elle existe. Une date peut être annoncée après accord du lieu, sans attendre l’équipe complète ou l’ouverture de la billetterie.
- En l’absence de dates validées, afficher un état clair et utile sans inventer d’événement.
- Des publications Instagram réelles et identifiées sont visibles dans la page avec un lien vers leur source ; alimentation manuelle initiale proposée, sans prétendre à une synchronisation automatique. Si aucune sélection n’est disponible, afficher un état explicite en prévisualisation et convenir du contenu publiable.
- Documenter la procédure et le responsable de mise à jour ; ne pas connecter HatCast ou un service tiers sans décision préalable.

### 4. Valider, publier et vérifier

En tant qu’équipe de La Malice, nous voulons mettre en ligne une version relue et vérifiée, puis savoir la maintenir.

- Contrôler textes, dates, liens, droits et crédits des médias ; obtenir et consigner la validation éditoriale et de publication d’Émilie et la revue visuelle de Doudou.
- Vérifier le rendu réel sur mobile et ordinateur, les parcours, les ancres, les liens et les états sans contenu ; documenter les limites éventuelles.
- Appliquer le workflow Git du dépôt : branche et worktree dédiés, contrôles, intégration et publication après validations requises. Le push sur `main` déclenche GitHub Pages.
- Vérifier séparément le push, le résultat du déploiement GitHub Pages, le domaine et la page réellement servie ; prévoir une marche arrière adaptée avant publication.
- Fournir à l’équipe la procédure courte pour modifier les dates et les actualités.

## Contributions attendues

Émilie et Doudou : une photo horizontale principale, deux à quatre photos complémentaires, deux ou trois liens de publications Instagram, le logo de référence si différent de celui déjà disponible, crédits et autorisation de publication. Vidéo facultative. Patrice : dates, lieux et liens de billetterie disponibles. Émilie : contact public et validation des textes et du périmètre final. Responsable de mise à jour à désigner.

## Hors périmètre proposé

Nouvelle billetterie, boutique, espace interne, intégration automatique de l’agenda ou d’Instagram, changement ou achat de domaine, création de fiche Google et campagne d’avis. Ces derniers sujets peuvent être traités séparément. Le référencement local est un objectif ; aucun classement n’est garanti.

## Points ouverts et dépendances

Dates et médias à recevoir ; solution pour la sélection et la maintenance des actualités ; contact public ; validation d’Émilie et contribution visuelle de Doudou ; choix technique et ADR ; procédure et accès de publication. Le dépôt impose le passage par contexte, découverte, spec, architecture, epics et sprint planning avant Loop. Un brief de travail existe dans un autre worktree avec des fichiers non suivis : le préserver et le réconcilier dans le futur sujet. Ne pas considérer ce découpage comme un backlog BMAD final prêt à développer.

## Validation de publication — 14 novembre 2026

Émilie demande la mise en ligne de cette première version après présentation par Patrice dans le groupe WhatsApp WEB MALICE ; elle propose de faire les commentaires ensuite. Source : capture transmise par Patrice le 14 novembre 2026. Patrice autorise explicitement le déploiement en production. Émilie précise qu’elle maintient le Linktree, qui ne couvre pour le moment que les spectacles avec réservation. Cette approbation porte sur la mise en ligne de la version présentée ; la direction artistique pourra être travaillée ultérieurement.
