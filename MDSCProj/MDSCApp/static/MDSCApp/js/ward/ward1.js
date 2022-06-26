const dictionary = ['yeast', 'leuks', 'tumor', 'uveas', 'signs', 'pouch', 'rabid', 'scale', 'nasal', 'senna', 'nodal', 'osteo', 'crest', 'tidal', 'histo', 'fibre', 'caval', 'blood', 'snore', 'mater', 'lumen', 'micro', 'tonic', 'exude', 'situs', 'inula', 'fetid', 'epley', 'grave', 'femur', 'hyper', 'allen', 'cycle', 'vials', 'bipap', 'glial', 'canal', 'scabs', 'wells', 'optic', 'actin', 'doula', 'limps', 'fugax', 'cipro', 'acids', 'groin', 'eosin', 'drips', 'flood', 'hinds', 'biota', 'toxin', 'slits', 'greys', 'mutes', 'wombs', 'soles', 'vulva', 'rinne', 'glans', 'ankle', 'heart', 'osler', 'burst', 'germs', 'sinus', 'hilar', 'chase', 'clone', 'scald', 'mucin', 'atony', 'urase', 'leech', 'cough', 'sores', 'death', 'covid', 'wards', 'fifth', 'trace', 'manic', 'biome', 'fetus', 'cilia', 'agent', 'nsaid', 'dnase', 'strip', 'cavae', 'enema', 'botox', 'itchy', 'loins', 'puffs', 'sting', 'vital', 'toxic', 'knees', 'spiny', 'tubal', 'semen', 'leaky', 'index', 'lumps', 'fists', 'rigor', 'potts', 'steth', 'fleet', 'kinin', 'croup', 'focus', 'bleed', 'leads', 'cysts', 'filum', 'venom', 'rnase', 'turps', 'chemo', 'ovary', 'rehab', 'animi', 'right', 'golgi', 'ictus', 'gumma', 'fever', 'auras', 'heinz', 'benzo', 'flaps', 'sonic', 'lletz', 'mumps', 'dosed', 'still', 'dural', 'pedis', 'titre', 'cheek', 'bones', 'alive', 'lymph', 'viral', 'siren', 'elute', 'fluid', 'axial', 'ulnar', 'durae', 'beard', 'boobs', 'talus', 'lobar', 'prism', 'curer', 'titer', 'radio', 'breed', 'assay', 'focal', 'vagal', 'sweet', 'flare', 'radii', 'lasix', 'ileum', 'sabin', 'crazy', 'varus', 'genus', 'pupil', 'folic', 'vagus', 'knots', 'ictal', 'prion', 'loops', 'jerky', 'blink', 'veins', 'valve', 'hellp', 'patau', 'tears', 'schiz', 'quack', 'berry', 'drain', 'ramus', 'hives', 'scars', 'break', 'elbow', 'sperm', 'abort', 'spurs', 'roots', 'yield', 'chyle', 'avian', 'salty', 'sharp', 'cocci', 'orbit', 'crude', 'casts', 'pubes', 'foods', 'moles', 'anvil', 'crabs', 'epsom', 'tract', 'volar', 'warty', 'tophi', 'salve', 'carpi', 'raphe', 'penis', 'atoms', 'folds', 'vitro', 'flesh', 'acini', 'lungs', 'nexus', 'ricin', 'lobes', 'clots', 'shiga', 'butts', 'smell', 'haart', 'elisa', 'lives', 'bruit', 'nails', 'rigid', 'medic', 'chart', 'touch', 'sugar', 'chins', 'cusps', 'venae', 'pharm', 'bolus', 'lysis', 'spasm', 'helix', 'belly', 'stone', 'agony', 'lipid', 'stain', 'shaft', 'lyses', 'hears', 'atlas', 'anums', 'apron', 'zonal', 'rheum', 'staph', 'vault', 'bulbs', 'ambos', 'myoma', 'deoxy', 'child', 'naked', 'backs', 'pumps', 'heals', 'puffy', 'phage', 'gauge', 'macro', 'gland', 'oaths', 'fovea', 'nigra', 'cells', 'rugae', 'nerve', 'colds', 'milli', 'lasik', 'wound', 'ewing', 'twins', 'tachy', 'pains', 'caths', 'polio', 'sweat', 'heels', 'scrub', 'navel', 'opsin', 'bejel', 'palsy', 'bumps', 'typhi', 'exons', 'axons', 'bloat', 'grays', 'panic', 'cocks', 'hymen', 'malic', 'spine', 'tests', 'preop', 'fused', 'broke', 'septa', 'limbs', 'lysed', 'osmol', 'resus', 'leucs', 'arcus', 'choke', 'hapto', 'faces', 'audio', 'patho', 'mania', 'acute', 'pubis', 'foley', 'cones', 'serum', 'algae', 'stunt', 'digit', 'xanax', 'jerks', 'lupus', 'peeps', 'human', 'wheal', 'dynia', 'labia', 'sprue', 'spina', 'necks', 'wrist', 'bowel', 'skull', 'siadh', 'water', 'weber', 'chest', 'shins', 'thigh', 'ortho', 'crypt', 'churg', 'bites', 'basic', 'vivax', 'stria', 'horns', 'petri', 'taxon', 'doses', 'lobed', 'swine', 'joint', 'nares', 'ergot', 'rosea', 'cramp', 'prime', 'ports', 'shock', 'gyrus', 'basal', 'leper', 'torso', 'swabs', 'broth', 'crust', 'flank', 'hilum', 'agars', 'genes', 'snuff', 'polyp', 'spike', 'tubes', 'ovale', 'shunt', 'blind', 'vocal', 'coags', 'thumb', 'sachs', 'smoke', 'noses', 'voice', 'phase', 'paget', 'field', 'aorta', 'iliac', 'coele', 'burns', 'joule', 'ilium', 'hypha', 'dummy', 'pulse', 'trunk', 'fatty', 'yolks', 'crown', 'sinew', 'retic', 'tinea', 'obese', 'corns', 'caput', 'virus', 'pubic', 'psoas', 'apgar', 'theca', 'nudes', 'brady', 'dying', 'umbra', 'scans', 'cruzi', 'bifid', 'bulla', 'cleft', 'sound', 'stoma', 'scaly', 'zonae', 'velum', 'hairs', 'nurse', 'erect', 'atria', 'bases', 'scalp', 'uvula', 'bends', 'calyx', 'tooth', 'crick', 'flora', 'chyme', 'aging', 'blots', 'aster', 'sebum', 'nitro', 'grams', 'numbs', 'snare', 'dorsi', 'parvo', 'palms', 'falls', 'rubor', 'locus', 'stool', 'ulcer', 'incus', 'torch', 'waist', 'locum', 'tunic', 'colon', 'natal', 'whorl', 'triad', 'laesa', 'fetor', 'vomit', 'liver', 'skins', 'ileus', 'drugs', 'hands', 'uveae', 'tonus', 'grips', 'smear', 'nidus', 'spots', 'boils', 'vater', 'lucid', 'salts', 'crush', 'urine', 'cajal', 'uncal', 'stage', 'shave', 'birth', 'warts', 'utero', 'waste', 'throb', 'fetal', 'supra', 'pauci', 'rales', 'renal', 'sleep', 'codon', 'myons', 'syrup', 'fossa', 'bursa', 'shear', 'gonad', 'urate', 'sling', 'renin', 'primi', 'detox', 'fungi', 'downs', 'biles', 'fundi', 'conal', 'cauda', 'pores', 'sulci', 'jelly', 'hyoid', 'stats', 'ulnas', 'reyes', 'dolor', 'varum', 'doser', 'nodes', 'hairy', 'ratio', 'pinna', 'pearl', 'flail', 'uveal', 'duras', 'drone', 'colic', 'pills', 'spore', 'acnes', 'decay', 'ulnae', 'boney', 'spiro', 'terms', 'wilms', 'error', 'dicks', 'ebola', 'model', 'krebs', 'tibia', 'trial', 'ranke', 'atopy', 'ostia', 'infra', 'donor']

const WORD_LENGTH = 5
const FLIP_ANIMATION_DURATION = 500
const DANCE_ANIMATION_DURATION = 500
const keyboard = document.querySelector("[data-keyboard]")
const alertContainer = document.querySelector("[data-alert-container]")
const guessGrid = document.querySelector("[data-guess-grid]")
const targetWord = 'heart'

startInteraction()

function startInteraction() {
  document.addEventListener("click", handleMouseClick)
  document.addEventListener("keydown", handleKeyPress)
}

function stopInteraction() {
  document.removeEventListener("click", handleMouseClick)
  document.removeEventListener("keydown", handleKeyPress)
}

function handleMouseClick(e) {
  if (e.target.matches("[data-key]")) {
    pressKey(e.target.dataset.key)
    return
  }

  if (e.target.matches("[data-enter]")) {	
    submitGuess()
    return
  }

  if (e.target.matches("[data-delete]")) {
    deleteKey()
    return
  }
}

function handleKeyPress(e) {
  if (e.key === "Enter") {
    submitGuess()
    return
  }

  if (e.key === "Backspace" || e.key === "Delete") {
    deleteKey()
    return
  }

  if (e.key.match(/^[a-z]$/)) {
    pressKey(e.key)
    return
  }
}

function pressKey(key) {
  const activeTiles = getActiveTiles()
  if (activeTiles.length >= WORD_LENGTH) return
  const nextTile = guessGrid.querySelector(":not([data-letter])")
  nextTile.dataset.letter = key.toLowerCase()
  nextTile.textContent = key
  nextTile.dataset.state = "active"
}

function deleteKey() {
  const activeTiles = getActiveTiles()
  const lastTile = activeTiles[activeTiles.length - 1]
  if (lastTile == null) return
  lastTile.textContent = ""
  delete lastTile.dataset.state
  delete lastTile.dataset.letter
}

function submitGuess() {
  const activeTiles = [...getActiveTiles()]
  if (activeTiles.length !== WORD_LENGTH) {
    showAlert("Not enough letters")
    shakeTiles(activeTiles)
    return
  }

  const guess = activeTiles.reduce((word, tile) => {
    return word + tile.dataset.letter
  }, "")

  if (!dictionary.includes(guess)) {
    showAlert("Not in ward list")
    shakeTiles(activeTiles)
    return
  }

  stopInteraction()
  activeTiles.forEach((...params) => flipTile(...params, guess))
}

function flipTile(tile, index, array, guess) {
  const letter = tile.dataset.letter
  const key = keyboard.querySelector(`[data-key="${letter}"i]`)
  setTimeout(() => {
    tile.classList.add("flip")
  }, (index * FLIP_ANIMATION_DURATION) / 2)

  tile.addEventListener(
    "transitionend",
    () => {
      tile.classList.remove("flip")
      if (targetWord[index] === letter) {
        tile.dataset.state = "correct"
        key.classList.add("correct")
      } else if (targetWord.includes(letter)) {
        tile.dataset.state = "wrong-location"
        key.classList.add("wrong-location")
      } else {
        tile.dataset.state = "wrong"
        key.classList.add("wrong")
      }

      if (index === array.length - 1) {
        tile.addEventListener(
          "transitionend",
          () => {
            startInteraction()
            checkWinLose(guess, array)
          },
          { once: true }
        )
      }
    },
    { once: true }
  )
}

function getActiveTiles() {
  return guessGrid.querySelectorAll('[data-state="active"]')
}

function showAlert(message, duration = 1000) {
  const alert = document.createElement("div")
  alert.textContent = message
  alert.classList.add("alert")
  alertContainer.prepend(alert)
  if (duration == null) return

  setTimeout(() => {
    alert.classList.add("hide")
    alert.addEventListener("transitionend", () => {
      alert.remove()
    })
  }, duration)
}

function shakeTiles(tiles) {
  tiles.forEach(tile => {
    tile.classList.add("shake")
    tile.addEventListener(
      "animationend",
      () => {
        tile.classList.remove("shake")
      },
      { once: true }
    )
  })
}

function checkWinLose(guess, tiles) {
  if (guess === targetWord) {
    showAlert("WELL DONE", 5000)
    danceTiles(tiles)
    stopInteraction()
    return
  }

  const remainingTiles = guessGrid.querySelectorAll(":not([data-letter])")
  if (remainingTiles.length === 0) {
    showAlert('REFRESH PAGE TO TRY AGAIN', null)
    stopInteraction()
  }
}

function danceTiles(tiles) {
  tiles.forEach((tile, index) => {
    setTimeout(() => {
      tile.classList.add("dance")
      tile.addEventListener(
        "animationend",
        () => {
          tile.classList.remove("dance")
        },
        { once: true }
      )
    }, (index * DANCE_ANIMATION_DURATION) / 5)
  })
}
