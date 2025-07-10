import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

i18n.use(initReactI18next).init({
  resources: {
    en: { translation: { "Welcome": "Welcome to NyayaVarta" } },
    hi: { translation: { "Welcome": "न्यायवर्त में आपका स्वागत है" } },
  },
  lng: "en",
  fallbackLng: "en",
  interpolation: { escapeValue: false },
});

export default i18n;
