(use-modules (guix build-system python)
             (guix git-download)
             (guix licenses)
             (guix packages)
             (gnu packages python-web)
             (gnu packages gettext)
             (gnu packages glib))

(package
  (name "ibus-theme-tools")
  (version "4.2.0")
  (source
   (origin
     (method git-fetch)
     (uri (git-reference
           (url "https://github.com/openSUSE/IBus-Theme-Tools")
           (commit (string-append "v" version))))
     (file-name (git-file-name name version))
     (sha256
      (base32
       "0i8vwnikwd1bfpv4xlgzc51gn6s18q58nqhvcdiyjzcmy3z344c2"))))
  (build-system python-build-system)
  (arguments
   `(#:tests? #f)) ; No tests
  (propagated-inputs
   `(("python-tinycss2" ,python-tinycss2)
     ("python-pygobject" ,python-pygobject)))
  (native-inputs
   `(("gettext" ,gettext-minimal)))
  (home-page "https://github.com/openSUSE/IBus-Theme-Tools")
  (synopsis "Tool for IBus Themes")
  (description "IBus Theme Tools can extract IBus-specific settings from
GTK themes to apply both within and without GNOME Shell.")
  (license gpl3+))
