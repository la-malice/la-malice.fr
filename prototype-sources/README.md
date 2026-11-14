# Prototype isolé des sources

Ce prototype reprend le contrat de transformation de `/private/tmp/la-malice-instagram-prototype-autonome/collecte.py` avec une fixture fictive. Il ne collecte pas Instagram ; le relevé réel existant est manuel et ses URL d'images peuvent expirer. `instagram.py` accepte une liste vide valide et refuse une réponse incohérente.

`spectacles.py` prend les deux titres Linktree relevés manuellement. Il conserve les titres et liens sans déduire l'année. `ia_spectacles.py` est un essai optionnel sur ce fichier local : il exige OPENAI_MODEL et OPENAI_API_KEY, utilise Responses avec JSON Schema et vérifie titres, liens, année et lieu. Un appel est facturé séparément : ne le lancer qu'avec budget et accès autorisés. Ne jamais placer la clé dans les fichiers ou journaux. La validation ne démontre pas que tous les champs générés sont corrects.

Le workflow `spike-sources.yml` ne traite que des fixtures. Il produit un artefact temporaire de démonstration, sans déploiement. Son horaire proposé ne s'exécutera pas depuis cette branche : GitHub exécute les workflows planifiés sur la branche par défaut. Ne pas intégrer ce workflow en production comme collecte fonctionnelle. Aucun accès Linktree ou Instagram, aucun appel IA et aucune conservation durable ne sont configurés.

Exécution locale : `python3 instagram.py fixtures/instagram.json /tmp/instagram-spike.json` et `python3 spectacles.py fixtures/spectacles.json /tmp/spectacles-spike.json`. Pour l'essai IA, définir la clé et le modèle dans l'environnement et lancer `python3 ia_spectacles.py fixtures/spectacles.json /tmp/spectacles-ia.json` après autorisation du coût.

À résoudre avant emploi réel : accès aux sources et conditions fournisseurs, récupération des vrais médias et expiration, classification des événements, année, validation métier, persistance fiable de la dernière collecte, suppression et état vide, alertes et coordination des déploiements. Le workflow existant de production et le site n'ont pas été modifiés.

`python3 demo.py /tmp/malice-demo-sortie` génère une page HTML et les deux JSON depuis les fixtures ; le dossier de sortie doit être nouveau. `python3 -m unittest discover -s . -p 'test_*.py'` exécute les contrôles. Le job IA utilise exclusivement l'environnement GitHub `github-pages`, avec le secret `OPENAI_API_KEY` et la variable `OPENAI_MODEL` de cet environnement ; il ne tourne que sur déclenchement manuel avec l'option cochée. Le job planifié simulé ne consomme aucun secret.
