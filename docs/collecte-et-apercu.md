# Collecte et aperçu des cartes

## Du Mac à GitHub

Le LaunchAgent `fr.la-malice.collecte-sources` lance la collecte à 8 h 17, 14 h 17 et 20 h 17, heure du Mac. Sa configuration se trouve dans `~/Library/LaunchAgents/fr.la-malice.collecte-sources.plist`. Les scripts et le journal `collecte.log` se trouvent dans `~/Library/Application Support/La Malice Sources/`.

- `collecter-et-envoyer.py` lance `collecter.py`, puis obtient un jeton temporaire auprès de la GitHub App LaMaliceDataScrap.
- `collecter.py` collecte Instagram et Linktree et prépare `sources.json`. La clé privée de l’app reste dans le dossier local du job.
- `envoyer.py` compare le JSON normalisé à celui de la branche `data/sources-sociales`. Un contenu identique produit le message « Données identiques ». Un contenu différent crée un commit qui contient le JSON et le pousse sur cette branche.

Un aperçu utilise le JSON distant. Pour diagnostiquer un écart, vérifier d’abord si le dernier contenu collecté a été poussé. Lire le journal ou consulter l’état du job avec `launchctl print gui/$(id -u)/fr.la-malice.collecte-sources`.

## Générer les cartes

Le workflow [spike-sources.yml](../.github/workflows/spike-sources.yml) lance le job manuel `apercu-sources` depuis `main`. Le runner récupère le code du site et place la branche de données dans `donnees-sociales/`. Le script [apercu_sources.py](../prototype-sources/apercu_sources.py) prend le JSON et [index.html](../index.html), puis écrit `apercu/index.html`. Le job joint ce fichier et ses ressources à l’exécution sous le nom `apercu-sources-sociales`.

- **Spectacles**. Le script traite jusqu’à six objets contenant `titre`, `url` et éventuellement `billetterie`. Le modèle reçoit le titre Linktree et les informations de billetterie disponibles. Le lien de réservation vient du JSON.
- **Instagram**. Le script examine les trois premières entrées. Une carte générée utilise `url`, `date_publication` au format ISO, `description_source` et `image` sous forme d’URL de données. Le modèle reçoit le visuel et la description. La date affichée vient directement du JSON. Les anciennes entrées qui contiennent seulement une URL sont ignorées par le générateur.
- **Insertion**. Pour chaque type, le script supprime les anciens articles correspondants et insère les nouvelles cartes à la place du premier. Il cherche précisément `<article class="panel event">` et `<article class="panel post">`. Si aucun article n’est généré pour un type, ses cartes existantes restent affichées.

Le job lit le secret `OPENAI_API_KEY` et la variable `OPENAI_MODEL` dans l’environnement GitHub `github-pages`.

## Vérifier un changement

Les tests du prototype se lancent avec `python3 -B -m unittest discover -s prototype-sources -p 'test_*.py'`. Pour tester la génération complète sur GitHub, lancer le workflow avec l’option `apercu_sources` sur `main` :

```sh
gh workflow run spike-sources.yml --repo la-malice/la-malice.fr --ref main -f apercu_sources=true
```

Télécharger l’artefact, extraire son contenu et ouvrir `index.html` en gardant `assets/` à côté. Vérifier les deux rubriques sur mobile, notamment les visuels, les dates, les liens et les informations de billetterie. Une exécution verte prouve que le fichier a été généré. La vérification du contenu et du rendu se fait sur l’aperçu.

L’[exécution 43632629356](https://github.com/la-malice/la-malice.fr/actions/runs/43632629356) a validé le job d’aperçu au commit `cc4e9a1`. La prise en compte de la billetterie dans le générateur a été vérifiée dans le code du commit `de52df0`. Au 14 novembre 2026, la branche de données contient trois entrées Instagram enrichies et deux spectacles avec un champ de billetterie.

La génération sur push de la branche de données et la publication automatique des cartes restent à raccorder. Suivre [les règles de livraison](WORKFLOW.md) avant un changement de publication.
