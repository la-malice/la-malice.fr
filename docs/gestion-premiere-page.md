# Mettre à jour la première page

Émilie a demandé la mise en ligne de la version présentée le 14 novembre 2026 et prévoit des commentaires ensuite ; la direction visuelle pourra être retravaillée avec Doudou. Les dates, médias, crédits, coordonnées, responsable et relais restent à confirmer. La photo d’accueil `assets/img/accueil-essai.webp` est un essai fourni par Patrice ; elle a été présentée à Émilie ; son crédit reste à préciser. Vérifier cette procédure avec le responsable et son relais lorsqu’ils seront désignés.

## Préparer les contenus

Dans `index.html`, les commentaires `DATES`, `ACTUALITÉS`, `MÉDIAS` et `CONTACT` repèrent les zones à modifier. Les dates et les actualités ont chacune une seule zone source. Pour chaque date confirmée par le lieu, indiquer titre, date et lieu, puis un lien de réservation s’il existe ; la date peut être annoncée sans billetterie. Sans date, conserver le message et les liens sociaux. Ne pas créer d’événement fictif.

Les deux cartes de la rubrique dates sont actuellement saisies manuellement depuis le Linktree de La Malice. Vérifier chaque événement et son lien avant publication, retirer les dates passées et conserver les dates futures ou l’état vide. Pour le spectacle du 20 novembre, l’horaire est laissé à la billetterie en raison d’indications divergentes.

Pour chaque publication autorisée, ajouter un visuel local autorisé, un texte alternatif utile, le crédit confirmé et un lien vers la publication source. Sans sélection, conserver le lien Instagram. N’ajouter que des photos réelles autorisées avec crédits confirmés ; laisser l’emplacement en attente si elles manquent. Les coordonnées directes nécessitent confirmation. Faire relire les textes existants avant publication.

La sélection provisoire affichée dans la zone `ACTUALITÉS` suit l’ordre des cartes HTML : 13 novembre, 11 novembre, puis 24 octobre 2026. Ses fichiers sont respectivement `assets/img/instagram/agenda-13-novembre-2026.jpg`, `assets/img/instagram/retrouvailles-11-novembre-2026.jpg` et `assets/img/instagram/retrouvailles-24-octobre-2026.jpg`. La sélection a été présentée pour cette première version ; les droits et crédits restent à documenter avec l’équipe. Pour modifier la sélection, remplacer ou réordonner les cartes dans cette unique zone, ajouter les fichiers locaux autorisés et leurs textes alternatifs, liens sources et crédits confirmés ; retirer de la liste positive les images qui ne sont plus utilisées. Si aucune sélection n’est autorisée ou disponible, supprimer les cartes et conserver un message indiquant que la sélection est en préparation ainsi que le lien permanent vers Instagram. Si une image échoue, son texte alternatif et le lien de sa carte vers la publication source restent accessibles.

Chaque nouveau fichier public doit être ajouté explicitement à la liste `files` de `scripts/build-pages.sh` ; ne jamais y ajouter de document interne. Préserver `CNAME` et la route `festival-impro-malice-2026.html`.

## Vérifier et publier

Depuis le worktree du sujet, lancer `scripts/build-pages.sh /tmp/la-malice-pages-review` avec un chemin de sortie inexistant. Examiner l’inventaire, servir ce dossier localement (par exemple `python3 -m http.server 8000 --directory /tmp/la-malice-pages-review`) et tester la page, les liens, le clavier, les formats mobile et bureau et la route festival. Pour les évolutions suivantes, faire relire la prévisualisation, appliquer les corrections et tracer les validations nécessaires. Un test local ne remplace pas leur contrôle sur téléphone.

Après autorisation, suivre `docs/WORKFLOW.md` pour intégrer et publier depuis `main`. Un lancement manuel sur une autre branche ne doit pas déployer. Contrôler le résultat dans GitHub Actions, puis le domaine et HTTPS, la page réellement servie, ses liens et la route festival. Ne pas modifier le domaine sans vérification et décision.

## Retour arrière

Si nécessaire, créer sur une branche dédiée un nouveau commit restaurant les fichiers publics de la version précédente, le vérifier puis le faire intégrer et publier selon le workflow. Ne pas réécrire l’historique partagé. Contrôler à nouveau Actions, domaine, page et route festival après déploiement.
