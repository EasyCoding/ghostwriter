Name: ghostwriter
Version: 1.7.3
Release: 1%{?dist}

License: GPLv3+
Summary: Cross-platform, aesthetic, distraction-free Markdown editor
URL: https://github.com/wereturtle/%{name}
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5XmlPatterns)
#BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5WebKit)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Xml)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: hunspell-devel
BuildRequires: gcc-c++

%description
Ghostwriter is a text editor for Markdown, which is a plain text markup
format created by John Gruber. For more information about Markdown, please
visit John Gruber’s website at http://www.daringfireball.net.

Ghostwriter provides a relaxing, distraction-free writing environment,
whether your masterpiece be that next blog post, your school paper,
or your novel.

%prep
%autosetup
mkdir -p %{_target_platform}
sed -i 's@appdata/@metainfo/@g' %{name}.pro

%build
pushd %{_target_platform}
    %qmake_qt5 PREFIX=%{_prefix} ..
popd
%make_build -C %{_target_platform}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc CHANGELOG.md CONTRIBUTING.md CREDITS.md README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Sat Oct 27 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.3-1
- Initial SPEC release.
