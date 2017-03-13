%{?scl:%scl_package nodejs-extend}
%{!?scl:%global pkg_name %{name}}

# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename extend

Name:               %{?scl_prefix}nodejs-extend
Version:            3.0.0
Release:            3%{?dist}
Summary:            Port of jQuery.extend for node.js and the browser

License:            MIT
URL:                https://www.npmjs.org/package/extend
Source0:            https://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
# https://raw.githubusercontent.com/justmoon/node-extend/148e7270cab2e9413af2cd0cab147070d755ed6d/test/index.js
Source1:            test-index.js
BuildArch:          noarch
%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      %{?scl_prefix}nodejs-devel


%if 0%{?enable_tests}
BuildRequires:      %{?scl_prefix}npm(tape)
# ..and some more
%endif

%description
nodejs-extend is a port of the classic extend() method from jQuery. It behaves
as you expect.  It is simple, tried and true.

%prep
%setup -q -n package
install -D -p -m0644 %{SOURCE1} test/index.js

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/extend
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/extend

%nodejs_symlink_deps

%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
node test/index.js
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/extend/

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.0-3
- Rebuild for rhscl

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 29 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.0.0-1
- new version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Ralph Bean <rbean@redhat.com> - 2.0.1-1
- new version

* Tue Jul 22 2014 Ralph Bean <rbean@redhat.com> - 1.3.0-1
- Initial packaging for Fedora.
