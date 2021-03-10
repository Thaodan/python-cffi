%bcond_with tests

Name:           python-cffi
Version:        1.14.5
Release:        0
Summary:        Foreign Function Interface for Python to call C code
License:        MIT
URL:            https://github.com/sailfishos/python-cffi
Source0:        %{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  libffi-devel
BuildRequires:  gcc

# For tests:
BuildRequires:  gcc-c++

%description
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT\u2019s FFI.

%package -n python3-cffi
Summary:        Foreign Function Interface for Python 3 to call C code
%if %{with tests}
BuildRequires:  python3-pytest
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pycparser

%description -n python3-cffi
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT's FFI.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%py3_build


%install
%py3_install
rm -rf doc

%check
%if %{with tests}
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m pytest c/ testing/
%endif

%files -n python3-cffi
%license LICENSE
%{python3_sitearch}/cffi/
%{python3_sitearch}/_cffi_backend.*.so
%{python3_sitearch}/cffi-*-py%{python3_version}.egg-info/

