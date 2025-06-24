"use client"

import type React from "react"
import { createContext, useContext, useState, useEffect, type ReactNode } from "react"
import { useTranslation } from "react-i18next"

interface LanguageContextType {
  currentLanguage: string
  changeLanguage: (language: string) => void
  supportedLanguages: Array<{ code: string; name: string; native_name: string }>
}

const LanguageContext = createContext<LanguageContextType | undefined>(undefined)

export const useLanguage = () => {
  const context = useContext(LanguageContext)
  if (context === undefined) {
    throw new Error("useLanguage must be used within a LanguageProvider")
  }
  return context
}

interface LanguageProviderProps {
  children: ReactNode
}

export const LanguageProvider: React.FC<LanguageProviderProps> = ({ children }) => {
  const { i18n } = useTranslation()
  const [currentLanguage, setCurrentLanguage] = useState(i18n.language || "en")

  const supportedLanguages = [
    { code: "en", name: "English", native_name: "English" },
    { code: "hi", name: "Hindi", native_name: "हिंदी" },
    { code: "bn", name: "Bengali", native_name: "বাংলা" },
    { code: "te", name: "Telugu", native_name: "తెలుగు" },
    { code: "mr", name: "Marathi", native_name: "मराठी" },
    { code: "ta", name: "Tamil", native_name: "தமிழ்" },
    { code: "gu", name: "Gujarati", native_name: "ગુજરાતી" },
    { code: "kn", name: "Kannada", native_name: "ಕನ್ನಡ" },
    { code: "ml", name: "Malayalam", native_name: "മലയാളം" },
    { code: "pa", name: "Punjabi", native_name: "ਪੰਜਾਬੀ" },
  ]

  useEffect(() => {
    const savedLanguage = localStorage.getItem("preferred_language")
    if (savedLanguage) {
      changeLanguage(savedLanguage)
    }
  }, [])

  const changeLanguage = (language: string) => {
    setCurrentLanguage(language)
    i18n.changeLanguage(language)
    localStorage.setItem("preferred_language", language)
  }

  const value = {
    currentLanguage,
    changeLanguage,
    supportedLanguages,
  }

  return <LanguageContext.Provider value={value}>{children}</LanguageContext.Provider>
}
