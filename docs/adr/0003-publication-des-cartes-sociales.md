# Publication des cartes sociales

Patrice a validé l’aperçu et demandé l’activation de la publication automatique. Le site reste statique et utilise GitHub Pages.

Le collecteur du Mac compare le JSON normalisé à la dernière version sur la branche `data/sources-sociales`. Un changement donne lieu à un commit puis à un événement GitHub `social-sources-changed`. Une collecte identique ne déclenche aucune génération. Les mises à jour de `main` continuent de passer par le déploiement habituel.

Le workflow Pages lit les données courantes et utilise le générateur validé dans l’aperçu. Seul le HTML rendu rejoint l’artefact public. Si la génération échoue, le déploiement ne démarre pas et la page déjà en ligne reste servie.
