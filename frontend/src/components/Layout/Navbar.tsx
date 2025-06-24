"use client"

import type React from "react"
import { useState } from "react"
import { Link, useNavigate } from "react-router-dom"
import { useAuth } from "../../contexts/AuthContext"
import { useLanguage } from "../../contexts/LanguageContext"
import { useTranslation } from "react-i18next"
import {
  Bars3Icon,
  XMarkIcon,
  UserIcon,
  BookOpenIcon,
  ScaleIcon,
  LanguageIcon,
  MicrophoneIcon,
} from "@heroicons/react/24/outline"

const Navbar: React.FC = () => {
  const { user, logout } = useAuth()
  const { currentLanguage, changeLanguage, supportedLanguages } = useLanguage()
  const { t } = useTranslation()
  const navigate = useNavigate()
  const [isOpen, setIsOpen] = useState(false)
  const [showLanguageMenu, setShowLanguageMenu] = useState(false)

  const handleLogout = () => {
    logout()
    navigate("/")
  }

  return (
    <nav className="bg-blue-900 shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="flex items-center space-x-2">
              <ScaleIcon className="h-8 w-8 text-white" />
              <span className="text-white text-xl font-bold">NyayaVarta</span>
            </Link>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex items-center space-x-8">
            <Link
              to="/content"
              className="text-white hover:text-blue-200 px-3 py-2 rounded-md text-sm font-medium flex items-center space-x-1"
            >
              <BookOpenIcon className="h-4 w-4" />
              <span>{t("nav.content")}</span>
            </Link>
            <Link to="/modules" className="text-white hover:text-blue-200 px-3 py-2 rounded-md text-sm font-medium">
              {t("nav.modules")}
            </Link>
            <Link to="/legal-aid" className="text-white hover:text-blue-200 px-3 py-2 rounded-md text-sm font-medium">
              {t("nav.legalAid")}
            </Link>
            <Link
              to="/translation"
              className="text-white hover:text-blue-200 px-3 py-2 rounded-md text-sm font-medium flex items-center space-x-1"
            >
              <MicrophoneIcon className="h-4 w-4" />
              <span>{t("nav.translation")}</span>
            </Link>

            {/* Language Selector */}
            <div className="relative">
              <button
                onClick={() => setShowLanguageMenu(!showLanguageMenu)}
                className="text-white hover:text-blue-200 px-3 py-2 rounded-md text-sm font-medium flex items-center space-x-1"
              >
                <LanguageIcon className="h-4 w-4" />
                <span>{supportedLanguages.find((lang) => lang.code === currentLanguage)?.native_name}</span>
              </button>
              {showLanguageMenu && (
                <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-50">
                  {supportedLanguages.map((language) => (
                    <button
                      key={language.code}
                      onClick={() => {
                        changeLanguage(language.code)
                        setShowLanguageMenu(false)
                      }}
                      className={`block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 w-full text-left ${
                        currentLanguage === language.code ? "bg-blue-50 text-blue-900" : ""
                      }`}
                    >
                      {language.native_name} ({language.name})
                    </button>
                  ))}
                </div>
              )}
            </div>

            {user ? (
              <div className="flex items-center space-x-4">
                <Link
                  to="/dashboard"
                  className="text-white hover:text-blue-200 px-3 py-2 rounded-md text-sm font-medium"
                >
                  {t("nav.dashboard")}
                </Link>
                <Link
                  to="/profile"
                  className="text-white hover:text-blue-200 px-3 py-2 rounded-md text-sm font-medium flex items-center space-x-1"
                >
                  <UserIcon className="h-4 w-4" />
                  <span>{user.first_name || user.username}</span>
                </Link>
                <button
                  onClick={handleLogout}
                  className="bg-blue-700 hover:bg-blue-600 text-white px-4 py-2 rounded-md text-sm font-medium"
                >
                  {t("nav.logout")}
                </button>
              </div>
            ) : (
              <div className="flex items-center space-x-4">
                <Link to="/login" className="text-white hover:text-blue-200 px-3 py-2 rounded-md text-sm font-medium">
                  {t("nav.login")}
                </Link>
                <Link
                  to="/register"
                  className="bg-blue-700 hover:bg-blue-600 text-white px-4 py-2 rounded-md text-sm font-medium"
                >
                  {t("nav.register")}
                </Link>
              </div>
            )}
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden flex items-center">
            <button onClick={() => setIsOpen(!isOpen)} className="text-white hover:text-blue-200 p-2">
              {isOpen ? <XMarkIcon className="h-6 w-6" /> : <Bars3Icon className="h-6 w-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-blue-800">
            <Link
              to="/content"
              className="text-white hover:text-blue-200 block px-3 py-2 rounded-md text-base font-medium"
              onClick={() => setIsOpen(false)}
            >
              {t("nav.content")}
            </Link>
            <Link
              to="/modules"
              className="text-white hover:text-blue-200 block px-3 py-2 rounded-md text-base font-medium"
              onClick={() => setIsOpen(false)}
            >
              {t("nav.modules")}
            </Link>
            <Link
              to="/legal-aid"
              className="text-white hover:text-blue-200 block px-3 py-2 rounded-md text-base font-medium"
              onClick={() => setIsOpen(false)}
            >
              {t("nav.legalAid")}
            </Link>
            <Link
              to="/translation"
              className="text-white hover:text-blue-200 block px-3 py-2 rounded-md text-base font-medium"
              onClick={() => setIsOpen(false)}
            >
              {t("nav.translation")}
            </Link>
            {user ? (
              <>
                <Link
                  to="/dashboard"
                  className="text-white hover:text-blue-200 block px-3 py-2 rounded-md text-base font-medium"
                  onClick={() => setIsOpen(false)}
                >
                  {t("nav.dashboard")}
                </Link>
                <Link
                  to="/profile"
                  className="text-white hover:text-blue-200 block px-3 py-2 rounded-md text-base font-medium"
                  onClick={() => setIsOpen(false)}
                >
                  {t("nav.profile")}
                </Link>
                <button
                  onClick={() => {
                    handleLogout()
                    setIsOpen(false)
                  }}
                  className="text-white hover:text-blue-200 block px-3 py-2 rounded-md text-base font-medium w-full text-left"
                >
                  {t("nav.logout")}
                </button>
              </>
            ) : (
              <>
                <Link
                  to="/login"
                  className="text-white hover:text-blue-200 block px-3 py-2 rounded-md text-base font-medium"
                  onClick={() => setIsOpen(false)}
                >
                  {t("nav.login")}
                </Link>
                <Link
                  to="/register"
                  className="text-white hover:text-blue-200 block px-3 py-2 rounded-md text-base font-medium"
                  onClick={() => setIsOpen(false)}
                >
                  {t("nav.register")}
                </Link>
              </>
            )}
          </div>
        </div>
      )}
    </nav>
  )
}

export default Navbar
