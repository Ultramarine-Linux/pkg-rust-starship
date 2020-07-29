# Generated by rust2rpm 13
%bcond_without check

%global crate starship

Name:           rust-%{crate}
Version:        0.42.0
Release:        2%{?dist}
Summary:        Minimal, blazing-fast, and infinitely customizable prompt for any shell! ☄🌌️

# Upstream license specification: ISC
License:        ISC
URL:            https://crates.io/crates/starship
Source:         %{crates_source}
# Initial patched metadata
# * No vendored
Patch0:         starship-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Minimal, blazing-fast, and infinitely customizable prompt for any shell! ☄🌌️.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}
# * (MIT or ASL 2.0) and BSD
# * ASL 2.0
# * ASL 2.0 or Boost
# * ASL 2.0 or MIT
# * ISC
# * MIT
# * MIT or ASL 2.0
# * MPLv2.0
# * Unlicense or MIT
License:        ISC and ASL 2.0 and MIT and BSD and MPLv2.0

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/starship
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CONTRIBUTING.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+attohttpc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+attohttpc-devel %{_description}

This package contains library source intended for building other packages
which use "attohttpc" feature of "%{crate}" crate.

%files       -n %{name}+attohttpc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+battery-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+battery-devel %{_description}

This package contains library source intended for building other packages
which use "battery" feature of "%{crate}" crate.

%files       -n %{name}+battery-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+http-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-devel %{_description}

This package contains library source intended for building other packages
which use "http" feature of "%{crate}" crate.

%files       -n %{name}+http-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-devel %{_description}

This package contains library source intended for building other packages
which use "native-tls" feature of "%{crate}" crate.

%files       -n %{name}+native-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# https://github.com/starship/starship/issues/755
sed -i -e '/EXE_PATH/s|/debug/|/release/|' tests/testsuite/common.rs
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
%if %{with check}
echo 'git-core'
%endif

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.42.0-1
- Update to 0.42.0

* Sat May 16 19:47:50 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.41.3-1
- Update to 0.41.3

* Thu May 14 19:31:23 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.41.1-1
- Update to 0.41.1

* Tue May 05 2020 Josh Stone <jistone@redhat.com> - 0.41.0-1
- Update to 0.41.0

* Wed Apr 15 08:44:33 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.40.1-1
- Update to 0.40.1

* Tue Mar 24 06:47:58 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.38.1-1
- Update to 0.38.1

* Sat Mar 21 07:37:04 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.38.0-1
- Update to 0.38.0

* Thu Mar 19 11:08:35 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.37.0-2
- Update git2 to 0.13

* Tue Mar 03 2020 Josh Stone <jistone@redhat.com> - 0.37.0-1
- Update to 0.37.0

* Thu Feb 20 09:08:02 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.36.1-1
- Update to 0.36.1

* Sun Feb 16 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.36.0-2
- Fixup license list

* Thu Feb 13 05:20:12 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Tue Feb 11 13:28:47 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.35.1-1
- Update to 0.35.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 08:19:53 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.32.1-1
- Update to 0.32.1

* Thu Dec 19 14:06:54 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.30.1-3
- Run tests

* Fri Dec 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.30.1-2
- Update to 0.30.1

* Fri Dec 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.29.0-1
- Update to 0.29.0

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.27.0-1
- Update to 0.27.0

* Thu Nov 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.26.5-1
- Update to 0.26.5

* Mon Nov 25 10:54:30 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.26.4-1
- Initial package
